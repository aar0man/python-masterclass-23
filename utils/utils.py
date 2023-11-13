import time
import string
import random
import tempfile
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{total_time:.20f} seconds - {func.__name__}')
        return result
    return timeit_wrapper


def get_random_list(num_pairs=100000, max_length=100, no_duplicates=False, sorted=False):
    random_list = []
    for _ in range(num_pairs):
        random_list.append(''.join(random.choice(string.ascii_letters) for _ in range(max_length)))
    if no_duplicates:
        random_list = list(set(random_list))
    if sorted:
        random_list.sort()
    return random_list


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))


def write_data_to_file(data):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        for word, count in data:
            temp_file.write(f"{word}: {count}\n".encode('utf-8'))
        return temp_file.name


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
