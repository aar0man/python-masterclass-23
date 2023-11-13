import time
import threading
from utils.utils import timeit


def demo_func(number):
    time.sleep(number)
    print(number)


def fetch_demo_func(number):
    demo_func(number)


def execute_async(number):
    def _demo_func(number):
        time.sleep(number)
        print(number)

    timer = threading.Timer(number, _demo_func, (number,))
    timer.start()


@timeit
def run_demo_sync():
    for i in range(0, 5):
        fetch_demo_func(i)


@timeit
def run_demo_async():
    for i in range(0, 5):
        execute_async(i)


if __name__ == "__main__":
    run_demo_sync()
    run_demo_async()
