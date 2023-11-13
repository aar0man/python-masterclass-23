from utils.utils import timeit, get_random_list
from collections import defaultdict
from collections import Counter


@timeit
def counter_dict(_random_list):
    counter = {}
    for item in _random_list:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    return counter


@timeit
def counter_defaultdict(_random_list):
    counter = defaultdict(int)
    for item in _random_list:
        counter[item] += 1
    return counter


@timeit
def counter_default(_random_list):
    return Counter(_random_list)


@timeit
def counter_with_set(_random_list):
    return len(set(_random_list))


if __name__ == '__main__':
    random_list = get_random_list()
    counter_dict(random_list)
    counter_defaultdict(random_list)
    counter_default(random_list)
    counter_with_set(random_list)
