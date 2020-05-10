import cProfile
import timeit
import time
from functools import lru_cache

def a(life):
    for a in range(life):
        time.sleep(2)
        b()
def b():
    now = time.time()

    while(time.time() < now + 3):
        pass

@lru_cache(maxsize=32)
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

# cProfile.run("fibo(40)")
# time_exec = timeit.Timer(lambda: fibo(4)).timeit(number=100)
# print(time_exec)
