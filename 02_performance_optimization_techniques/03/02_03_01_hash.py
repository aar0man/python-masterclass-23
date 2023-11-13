from utils.utils import timeit


class CustomDict:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        entry = self.table[index]
        if entry is not None and entry[0] == key:
            return entry[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        entry = self.table[index]
        if entry is not None and entry[0] == key:
            self.table[index] = None
        return None


@timeit
def call_custom_dict():
    test_dict = CustomDict()
    test_dict.set("a", 1)
    test_dict.set("b", 2)

    # print(test_dict.get("a"))
    # print(test_dict.get("b"))
    # print(test_dict.get("c"))

    test_dict.remove("a")


@timeit
def call_default_dict():
    test_dict = dict(a=1, b=2)
    # test_dict = {"a": 1, "b": 2}

    # print(test_dict.get("a"))
    # print(test_dict.get("b"))
    # print(test_dict.get("c"))

    test_dict.pop("a")


if __name__ == '__main__':
    call_custom_dict()
    call_default_dict()
