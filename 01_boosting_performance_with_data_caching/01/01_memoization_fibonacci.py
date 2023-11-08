import time


memo = {}


def fibonacci_simple(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_simple(n - 1) + fibonacci_simple(n - 2)
    return result


def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    memo[n] = result
    return result


if __name__ == '__main__':
    print("fibonacci 30")
    start_time = time.perf_counter()
    fibonacci_simple(30)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.20f} seconds fibonacci_simple')

    start_time = time.perf_counter()
    fibonacci_memo(30)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.20f} seconds fibonacci_memo')
