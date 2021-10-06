def return_multiply(n):
    def cal(m):
        return m ** 2
    import multiprocessing    
    pool = multiprocessing.Pool(2)
    return pool.map(cal, n)