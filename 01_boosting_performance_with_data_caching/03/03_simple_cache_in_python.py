import time
from utils.utils import timeit

cache = {}


def expensive_operation(n):
    time.sleep(1)
    return n * 2


@timeit
def cached_operation(n):
    if n in cache:
        return cache[n]

    result = expensive_operation(n)
    cache[n] = result
    return result


if __name__ == '__main__':
    cached_operation(5)
    cached_operation(5)
