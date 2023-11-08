import asyncio


async def io_task(name):
    print(f'Starting I/O task {name}')
    await asyncio.sleep(2)
    print(f'Completed I/O task {name}')


async def cpu_task(name):
    print(f'Starting CPU task {name}')
    await asyncio.sleep(1)
    print(f'Completed CPU task {name}')


async def main():
    tasks = []
    for i in range(3):
        tasks.append(io_task(f'I/O-{i}'))
        tasks.append(cpu_task(f'CPU-{i}'))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
