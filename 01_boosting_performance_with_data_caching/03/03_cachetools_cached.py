import time
from cachetools import cached

from utils import timeit

cache = {}


@timeit
@cached(cache={})
def expensive_operation(n):
    time.sleep(1)
    return n * 2


if __name__ == '__main__':
    expensive_operation(5)
    expensive_operation(5)
