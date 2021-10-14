import multiprocessing
import time
import os

def return_multiply(n):
    
    print(f"{n}의 PID는 :",os.getpid(),"입니다.")
    time.sleep(0.1)
    return n ** 2

def single_processing():
    start = time.time()
    print(list(map(return_multiply, range(1, 20))))
    proc_time = time.time() - start
    print(round(proc_time, 1), "초")

def multi_processing():
    start = time.time()
    pool = multiprocessing.Pool(4)
    print(pool.map(return_multiply, range(1, 20)))
    proc_time = time.time() - start
    print(round(proc_time, 1), "초")

if __name__=="__main__":
    multi_processing()