from utils.utils import timeit, get_random_list
import bisect


@timeit
def list_search(_random_list):
    return _random_list.index('aa')


@timeit
def bisect_search(_random_list):
    return bisect.bisect(_random_list, 'aa')


@timeit
def bisect_most_left(_random_list):
    return bisect.bisect(_random_list, 'aa')


if __name__ == '__main__':
    # random_list = get_random_list(max_length=2, no_duplicates=True)
    random_list = get_random_list(max_length=2, no_duplicates=True, sorted=True)
    # random_list = ['aa', 'bb', 'cc', 'dd']

    print("sorted list")
    list_search(random_list)
    bisect_search(random_list)

    # print(list_search(random_list))
    # print(deques_search(random_list))

