import time


memo = {}


def knapsack_simple(values, weights, capacity, n):
    def knapsack_recursive(capacity, n):
        if n == 0 or capacity == 0:
            result = 0
        elif weights[n - 1] > capacity:
            result = knapsack_recursive(capacity, n - 1)
        else:
            include = values[n - 1] + knapsack_recursive(capacity - weights[n - 1], n - 1)
            exclude = knapsack_recursive(capacity, n - 1)
            result = max(include, exclude)

        return result

    return knapsack_recursive(capacity, n)


def knapsack_memo(values, weights, capacity, n):
    memo = {}

    def knapsack_recursive(capacity, n):
        if (capacity, n) in memo:
            return memo[(capacity, n)]

        if n == 0 or capacity == 0:
            result = 0
        elif weights[n - 1] > capacity:
            result = knapsack_recursive(capacity, n - 1)
        else:
            include = values[n - 1] + knapsack_recursive(capacity - weights[n - 1], n - 1)
            exclude = knapsack_recursive(capacity, n - 1)
            result = max(include, exclude)

        memo[(capacity, n)] = result
        return result

    return knapsack_recursive(capacity, n)


if __name__ == '__main__':
    values = [150, 220, 210, 170, 450, 270, 400, 560, 670, 190, 700, 120, 320, 250, 620, 600, 100, 180, 520, 640,
              320, 480, 400, 220, 500, 360, 160, 340, 150, 440, 370, 580, 280, 440, 680, 480, 790, 630, 430, 200, 460,
              640, 260, 490, 660, 440, 680, 510, 210, 790, 620, 340, 330, 280, 590, 660, 480, 280, 190, 400, 650, 570,
              220, 510, 640, 430, 300, 780, 750, 320, 660, 350, 600, 720, 580, 540, 860, 730, 290, 820, 330, 420, 770,
              680, 370, 150, 600, 790, 470, 260, 100, 590, 790, 770, 490, 600, 630, 510]

    weights = [70, 90, 120, 35, 100, 80, 95, 75, 110, 35, 150, 55, 40, 50, 65, 75, 25, 50, 65, 100,
               25, 40, 60, 50, 70, 30, 65, 40, 80, 90, 20, 45, 70, 90, 60, 20, 65, 25, 75, 25, 40, 60, 90, 30, 40, 65,
               45, 75, 35, 55, 60, 30, 20, 25, 60, 50, 40, 30, 45, 50, 60, 40, 65, 50, 80, 30, 85, 40, 65, 35, 60, 60,
               40, 70, 90, 55, 40, 30, 45, 70, 70, 45, 65, 30, 50, 35, 45, 85, 50, 30, 25, 60, 75, 55, 40, 60, 65, 45]
    capacity = 200
    n = len(values)

    start_time = time.perf_counter()
    max_value = knapsack_simple(values, weights, capacity, n)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.20f} seconds knapsack_simple')

    start_time = time.perf_counter()
    max_value = knapsack_memo(values, weights, capacity, n)

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.20f} seconds knapsack_memo')
