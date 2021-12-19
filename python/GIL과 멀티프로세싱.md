## GIL(Global Interpreter Lock, 전역 인터프리터 잠금)

멀티 스레딩은 스레드끼리 자원을 공유하는데, 하나의 자원을 동시에 여러 스레드가 가져가는 상황에서 충돌이 발생할 수 있다.

이 경우에 하나의 스레드에 문제가 생길 경우 다른 스레드에 의해 차단될 수 있다.

이러한 이유로 파이썬에서는 GILGlobal Interpreter Lock, 전역 인터프리터 잠금)를 도입하였다.

### GIL 이란?

한 번에 1개의 스레드만 유지하는 락이며, 하나의 스레드가 다른 스레드를 차단해서 제어를 얻는 것을 막아준다.

즉, 하나의 스레드가 문제가 생기더라도 다른 스레드에 의해서 차단되지 않게 한다.

이러한 이유로 파이썬에서는 스레드를 통해 CPU bound 코드에서 병렬성 연산을 수행하지 못한다.

단, Network I/O bound 코드에서는 멀티스레딩을 유의미하게 사용할 수 있다.

### 멀티 프로세싱(multi processing)

GIL 정책에 의해서 CPU bound 코드에서는 멀티 스레딩에 제한이 있다. 멀티 프로세싱은 CPU bound 코드에서도 병렬성을 지원한다.

하지만, 멀티 프로세싱은 멀티 스레드와 달리 독립적인 메모리에 저장하기 때문에 프로세스간 데이터 통신 등에서 발생하는 비용(직렬화, 역직렬화 등)은 감안해야한다.

아래는 cpu bound를 유발시키는 함수를 정의한 것이다. 코드는 [윤상석님의 강의 코드(teaching-async-python)](https://github.com/amamov/teaching-async-python)를 사용하였다.

싱글 프로세스-싱글 스레드로 실행시킨 것과 멀티스레딩, 멀티프로세싱으로 실행한 구문을 비교해보도록 하자.

```python
import time
import os
import threading

# nums = [50, 63, 32]
nums = [30] * 100

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    # CPU bound 함수
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total
```

##### Single Process Single Thread

```python
def main():
    results = [cpu_bound_func(num) for num in nums]
    return results
```

```
4228 process | 4684 thread
4228 process | 4684 thread
4228 process | 4684 thread
        ...
4228 process | 4684 thread
4228 process | 4684 thread
4228 process | 4684 thread
21.37012004852295
```

싱글프로세스에서 싱글스레드로 처리했을 때 약 21초 소요되었다.

##### Multi Thread

```python
from concurrent.futures import ThreadPoolExecutor

def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    return results
```

```
14172 process | 5568 thread, 30
14172 process | 13496 thread, 30
14172 process | 15344 thread, 30
        ...
14172 process | 8776 thread, 30
14172 process | 1160 thread, 30
14172 process | 15344 thread, 30
22.69828963279724
```

앞서 언급한 것과 같이 CPU bound 상황에서는 멀티스레딩으로 병렬처리를 하더라도 의미가 없다.

##### Multi Process
```python
from concurrent.futures import ProcessPoolExecutor

def main():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    return results
```

```
10128 process | 5596 thread, 30
17188 process | 9636 thread, 30
12940 process | 14072 thread, 30
        ...
15876 process | 14480 thread, 30
15384 process | 788 thread, 30
1704 process | 14064 thread, 30
15.954249143600464
```

CPU bound 상황에서 이전의 코드들보다 7초가 단축되었다.

### 결론

파이썬에서는 GIL 정책으로 멀티스레딩에 대한 제한이 있기 때문에, 각각의 상황에 따라 자원을 최적화하여 활용할 수 있는 방법을 찾아야한다.

위의 예제와 같이 CPU 집약적인 연산이 필요한 경우에는 멀티스레딩보다 멀티프로세스를 사용해야 할 것이며, 물론 각 서버의 자원에 따라 worker의 수를 잘 조절해야한다.

Network I/O Bound의 상황에서는 멀티스레딩이 유의미할 수 있지만, 가능한 하나의 스레드에서 동시에 처리 할 수 있도록 concurrency한 프로그래밍을 해야한다.
