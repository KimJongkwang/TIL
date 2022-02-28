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
