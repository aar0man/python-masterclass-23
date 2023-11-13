import threading
import concurrent.futures
import time
import asyncio
from utils.utils import timeit


def io_task(name):
    print(f'Starting I/O task {name}')
    time.sleep(2)
    print(f'Completed I/O task {name}')


def cpu_task(name):
    print(f'Starting CPU task {name}')
    time.sleep(1)
    print(f'Completed CPU task {name}')


@timeit
def using_threading():
    thread1 = threading.Thread(target=io_task, args=("I/O-1",))
    thread2 = threading.Thread(target=cpu_task, args=("CPU-1",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


@timeit
def using_futures():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(io_task, "I/O-2")
        future2 = executor.submit(cpu_task, "CPU-2")

    concurrent.futures.wait([future1, future2])


async def async_io_task(name):
    print(f'Starting I/O task {name}')
    await asyncio.sleep(2)
    print(f'Completed I/O task {name}')


async def async_cpu_task(name):
    print(f'Starting CPU task {name}')
    await asyncio.sleep(1)
    print(f'Completed CPU task {name}')


@timeit
async def using_asyncio():
    tasks = [
        async_io_task("I/O-3"),
        async_cpu_task("CPU-3")
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    print("Utilizare cu Threading:")

    using_threading()
    
    print("\nUtilizare cu Futures (Promisiuni):")
    using_futures()
    
    print("\nUtilizare cu Programarea Asincronă (Async, asyncio):")
    asyncio.run(using_asyncio())
