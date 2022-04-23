<!-- 현재 폐쇄망 내부에서 진행중인 프로젝트의 배치 파이프라인은 상당히 상호 의존적인 프로세스들이 많이 있는데, 특히 A - B - C의 순서로 파이프라인이 실행이 되지 않으면 작동하지 않는 비순환 그래프 구조의 파이프라인이 지배적으로 많다.

물론 이 파이프라인들도 shell에서 데몬을 통해 비순환적으로 실행 시킬 수 있지만, 입력받는 파라미터가 오늘 날짜를 받게 되는 경우가 있다.

이때에 A 스크립트에서 오늘 날짜를 받아 작동하고, 모종의 이유로 A의 런타임이 길어지게 됨에 따라 A에 의존적인 B 스크립트가 실행할 때 이튿날로 넘어가버리는 경우에는 파이프라인이 실행되지 않는 때가 있다.

처음에는 파이프라인의 최초 실행시간을 변수로하는 shell 스크립트 내에서 각각의 스크립트에 해당 시간을 주는 방법을 고안했었으나, 점차 실행해야할 스크립트가 많아져 관리해야할 파이프라인이 많아지게 됐을 때 버거움이 생겼다.

이러한 이유로 Apache-Airflow를 도입해보고자 하였다. 익숙한 python으로 관리하는 것과 UI로써 모니터링이 가능한 점, 강력한 backfill이 매력으로 다가왔다.

에어플로우를 설치한다. -->

## Install Airflow

Airflow 기본 동작 원리

![image](https://engineering.linecorp.com/wp-content/uploads/2021/01/k8sdataeng1-768x408.png)

> 그림 출처 [라인 기술 블로그](https://engineering.linecorp.com/ko/blog/data-engineering-with-airflow-k8s-1/)

- Scheduler - DAG와 Task를 모니터링하고 관리하는 역할, 주기적으로 실행할 Task들을 실행 가능한 상태로 변경한다.
- Webserver - Airflow UI서버
- Kerberos - 인증 처리를 위한 티켓 갱신 프로세스(선택사항)
- DAG Script - 개발자가 작성한 Python 워크플로 스크립트
- MetaDB - Airflow 메타데이터 저장소. DAG에 대한 등록 정보 등이 DB화됨
- Executor - Task 인스턴스를 실행하는 주체로 Sequential, Debug, Local, Dask, Celery, Kubernetes 등 다양한 Executor가 존재
- Worker - 실제 작업을 수행하는 주체이다

<!-- Python, bash, spark, Hive -->

1. 설치

공식문서에는 두 가지 설치 방법이 있다. local서버에 설치하는 방법과 docker위에 설치하는 방법으로 추후에 폐쇄망에서도 적용하고자 하여 local서버에 설치하는 방법으로 진행하고자 한다.

공식 페이지에 있는 설치 스크립트를 이용하여 Airflow를 설치해보도록 하겠다.

`vim ~/install_airflow.sh`
`sudo chmod 755 install_airflow.sh`

```bash
AIRFLOW_VERSION=2.2.2
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

> 이후 위의 스크립트를 실행시켜 설치하면된다. 그런데?<br> > `ModuleNotFoundError - No Module named \_ctypes` <br>
> 에러가 발생한다. 여러 디펜던시들이 설치가 안된다. 이유를 알고보니, 서버에 파이썬을 설치할 때 파이썬 디펜던시를 빼먹고 컴파일 했었다. <br> > `sudo yum install libffi-devel` libffi-devel 을 설치해주고 다시 컴파일하여 설치를 해주었다.

```bash
# airflow version
2.2.2
```

2. DB 초기화 및 설정 파일 수정

Airflow 설치 이후에는 Airflow의 meta db를 초기화 해주어야 한다. 메타DB는 SQLite에 기본으로 초기화된다.

또한, 기본 executor는 sequential executor로 병렬이 아니라 이름대로 순차적인 실행이다.

필자는 간단히 테스트 목적으로 local에서 병렬실행을 하기 위해 local executor로 변경과 이에 따라 DB도 postgresql에 초기화 하기로 하겠다.

보통 따로 설치경로를 잡지 않는다면 홈경로에 있다.

`vim ~/airflow/airflow.cfg`

![image](D:\JK\git-repo\TIL\DE\ApacheAirflow\Inkedairflow.cfg수정.png_LI.jpg)

이 외에도 샘플 task를 보지 않으려면 `load_examples = True`를 `False`로 변경하면 된다.

3. Simple DAG 만들기

DAG는 Directed Acyclic Graph(비 순환 그래프)로 말그대로 순환되지 않는 구조를 일컫는다.

예를 들어 A -> B -> C 각각이 종속적일 때 동작하며, A -> B -> A -> C 는 DAG 개념에서 벗어난 개념이다.

단, A -> B -> C, A -> C -> D 와 같이 트리가 꾸려지더라도 종속적으로 동작할 수 있다면 가능하다.

##### Default Arguments

default args는 각 DAG마다 정의한 Operator에 전달하는 기본 arguments들을 정의해놓은 것이다.
자주 사용되는 파라미터는 아래와 같다.

```python
default_args = {
    'owner': 'Airflow' # 각 테스크의 owner. linux username이 추천됨
    'start_date': datetime(2016, 1, 1), # 작업이 시작될 날짜
    'end_date': datetime(2016, 2, 1), # 이 날짜 이후로는 작업을 시행하지 않음
    'retries': 1, # 최대 재시도 횟수
    'retry_delay': timedelta(minutes=5), # 재시도 간 딜레이
    'depends_on_past': False, # true일 경우, 이전 분기 작업이 성공해야만 작업을 진행
    'on_failure_callback':some_function(), # task가 실패했을 경우 호출할 함수, dictype의 context를 전달.
    'on_retry_callback':some_function2(), # 재시도시, 상동
    'on_success_callback':some_function3(), # 성공시, 상동
    'priority_weight': 10, # 이 테스크의 우선순위 가중치, 높을 수록 먼저 triggered
}

dag = DAG('my_dag', default_args=default_args)
op = DummyOperator(task_id='dummy', dag=dag)
print(op.owner) # Airflow
```

##### Scope

Airflow는 DAGfile 의 모든 DAG 오브젝트를 불러올 수 있다. 다만 각 오브젝트는 전역변수이어야 한다.

##### Operator

Operator는 일반적으로 독립적으로 동작하기 때문에, 자원을 공유할 필요가 없다. DAG는 독립적으로 실행 순서만 지켜주면 된다. 만일 두 Operator가 파일, 데이터를 소량으로 공유해야할 경우에는 하나의 Operator로 합칠 수 있다. 또는 Airflow가 지원하는 XCom 기능을 활용 할 수 있다.

XCom은 추후에 필요시 알아보도록 하겠다.

Operator의 종류는 정말 많다. 그 중에 주로 사용되는 Operator들은 아래와 같다.

- bash, python, mysql, jdbc, hive, spark 등

##### Task

Operator가 인스턴스로 쓰이게 되면 Task라고 한다. 각각의 Task들은 DAG 그래프를 보았을 때 노드가 된다.

#### Error 모음

> Some workers seem to have died and gunicorn did not restart them as expected

- 해결

로그를 살펴보니, Airflow의 웹 인터페이스를 담당하는 gunicorn worker들이 정상적으로 실행되지 않았고, 이로 인해 웹 서버 자체가 사망하는 일이 발생했습니다. 설정이나 ECS task definition을 봐도 딱히 잘못된 부분이 없어보여서 조금 헤맸는데, 약간 살펴본 결과 메모리가 부족해서 생기는 문제였습니다. 웹 서버 container에 350MiB를 할당하고, gunicorn worker 수는 기본 설정값대로 4개를 사용 중이었는데 혹시나 해서 worker 개수를 3으로 줄이니 정상 실행되는 것을 확인할 수 있었습니다.

참고로, gunicorn worker 수는 airflow.cfg의 다음 섹션에서 찾으실 수 있습니다.

```cfg
[webserver]
# Number of workers to run the Gunicorn web server
workers = n
```

> don't connect scheduler port "0.0.0.0:8078"

- 해결

스케쥴러가 포트에 연결이 되지 않는다. 이전 서버를 데몬으로 실행시키면서 종료시킬 때 마스터를 종료시키고, 하위의 노드 프로세스들을 제거하지 않은 상태로 다시 서버를 재실행시킬 때 발생하였다.

모든 프로세스들을 kill 하고 난 후에 재실행하였을 때 문제없이 실행되었다.

```bash
kill -9 `ps aux | grep airflow | awk '{print $2}'` # airflow 전체
kill -9 $(ps -ef | grep "airflow scheduler" | awk '{print $2}') # scheduler
kill -9 $(ps -ef | grep "gunicorn" | awk '{print $2}') # gunicorn ## 주의 혹시나 실행 중인 gunicorn 서버가 있다면 실행하면 안됨.
```
