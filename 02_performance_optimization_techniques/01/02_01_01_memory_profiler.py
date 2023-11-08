import random
import string
from memory_profiler import profile


@profile
def test_function(num_pairs=10000, max_length=100):
	random_list = []
	for _ in range(num_pairs):
		random_list.append(''.join(random.choice(string.ascii_letters) for _ in range(max_length)))
	return random_list


if __name__ == "__main__":
	test_function()
