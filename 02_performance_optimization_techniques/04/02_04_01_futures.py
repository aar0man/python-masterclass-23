import threading
from concurrent.futures import Future
from utils.utils import timeit


def fetch_demo_func(number):
	future = Future()
	result = number
	timer = threading.Timer(number, lambda: future.set_result(result))
	timer.start()

	return future


def execute_async(number):
	_future = fetch_demo_func(number)

	def on_done_future(future):
		response = future.result()
		print(response)

	_future.add_done_callback(on_done_future)


@timeit
def run_demo_async():
	for i in range(0, 5):
		execute_async(i)


if __name__ == "__main__":
	run_demo_async()
