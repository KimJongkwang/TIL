import multiprocessing

def return_multiply(n):
    def cal(m):
        return m ** 2
    pool = multiprocessing.Pool(2)
    return pool.apply(cal(n))

