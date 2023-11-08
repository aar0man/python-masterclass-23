import time
import random
from utils import timeit


@timeit
def test_data_structure(data_structure, operation, data, num_iterations=1000):
    start_time = time.time()
    for _ in range(num_iterations):
        if operation == "insert":
            data_structure.insert(data)
        elif operation == "lookup":
            data_structure.lookup(data)
        elif operation == "delete":
            data_structure.delete(data)
    end_time = time.time()
    return end_time - start_time


class ListWrapper:
    def __init__(self):
        self.data = []

    def insert(self, data):
        self.data.append(data)

    def lookup(self, data):
        return data in self.data

    def delete(self, data):
        if data in self.data:
            self.data.remove(data)


class DictWrapper:
    def __init__(self):
        self.data = {}

    def insert(self, data):
        self.data[str(data)] = data

    def lookup(self, data):
        return str(data) in self.data

    def delete(self, data):
        key = str(data)
        if key in self.data:
            del self.data[key]


data_to_insert = [random.randint(1, 100000) for _ in range(100000)]
data_to_lookup = random.choice(data_to_insert)
data_to_delete = random.choice(data_to_insert)

print("insert")

test_data_structure(ListWrapper(), "insert", data_to_insert)
test_data_structure(DictWrapper(), "insert", data_to_insert)

print()
print("lookup")

test_data_structure(ListWrapper(), "lookup", data_to_lookup)
test_data_structure(DictWrapper(), "lookup", data_to_lookup)

print()
print("delete")

test_data_structure(DictWrapper(), "delete", data_to_delete)
test_data_structure(ListWrapper(), "delete", data_to_delete)
