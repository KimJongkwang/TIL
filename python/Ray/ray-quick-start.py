import ray
import datetime
import time

print(ray.__version__)


# Ray Task(Remote Function) 정의
@ray.remote
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    # print(current_datetime)
    return current_datetime


# common
if __name__=="__main__":
    """
    1) ray.init(): 드라이버실행, cpu, gpu 갯수, Ray cluster 연결정보, 대시보드 정보 등의 인자
        - ex) ray.init(address="192.168.0.100:5000", ignore_reinit_error=True)
    2) @ray.remote: 파이썬 함수나 클래스를 다른 프로세스에서 실행되는 Ras Task로 만들어주는 데코레이터, 필요시 인자를 받을 수 있음(num_gpus, max_calls등)
    3) .remote(): Remote Function, Class(@ray.remote로 래핑한 함수나 클래스) 선언 호출시 사용하는 접미사, 기존 함수의 인자를 받을 수 있음
        - Remote 작업은 비동기적 실행(asynchronous)
        - func.remote(x)
        - actor = SomeClass.remote()
        - actor_obj = actor.method_a.remote(y)
    4) ray.put(): Object를 저장하고 ID 반환
        - put은 동기적 실행
    5) ray.get(): ObjectRef(Object Id)를 받아 Object Value를 반환
    6) ray.wait(): 준비된 Object Id와 준비되지 않은 Object Id반환, Task가 완료될 때까지 기다림
        - if ray.wait()[-1] is None:
            run_function()
    7) ray.shutdown(): ray.init으로 시작된 프로세스를 종료하고 워커와 연결을 끊음
        - Ray를 사용한 파이썬 프로세스가 종료되면 자동으로 이 코드가 실행됨
    """
    # ray.init()은 최초에 선언하여 초기화
    # ray task를 래핑한 함수를 호출하면 ray를 호출, 이후에 다시 초기화하면 아래와 같은 런타임 에러 발생(init은 대쉬보드 호출)
    # RuntimeError: Maybe you called ray.init twice by accident? This error can be suppressed by passing in 'ignore_reinit_error=True' or by calling 'ray.shutdown()' prior to 'ray.init()'.
    ray.init()

    
    



    # Ray Task로 래핑된 함수는 일반 함수로 호출하면 Type Error 발생
    # print_current_datetime()
    # TypeError: Remote functions cannot be called directly. Instead of running '__main__.print_current_datetime()', try '__main__.print_current_datetime.remote()'.

    # 위에서 말한대로 remote()를 붙여 실행하였더니 ObjectRef(a67dc375e60ddd1affffffffffffffffffffffff0100000001000000) 객체가 리턴됨

    # print(print_current_datetime.remote(), "!!?")
    # print(ray.get(print_current_datetime.remote())) # ray.get으로 값을 얻을 수 있다.
    # ObjectRef(a67dc375e60ddd1affffffffffffffffffffffff0100000001000000) !!?
    # 2021-12-01 10:00:37.028593

    # 그런데 의아한 점! 함수에서 print()를 줄땐  pid=41312) 2021-12-01 10:00:03.747540와 같이 pid가 함께 리턴됨.
    data = [print_current_datetime.remote() for i in range(20)]
    print(ray.get(data))

    # ray.shutdown()
