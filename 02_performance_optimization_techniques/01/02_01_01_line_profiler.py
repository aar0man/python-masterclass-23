import random
import string
from line_profiler import LineProfiler

lp = LineProfiler()


def test_function(num_pairs=100000, max_length=100):
    random_list = []
    for _ in range(num_pairs):
        random_list.append(''.join(random.choice(string.ascii_letters) for _ in range(max_length)))
    return random_list


if __name__ == "__main__":
    lp.add_function(test_function)
    lp.run("test_function()")

    lp.print_stats()
