import asyncio


async def ServiciuA():
    print("Serviciu A: Inițierea secvenței...")
    await asyncio.sleep(1)
    await ServiciuB()


async def ServiciuB():
    print("Serviciu B: Execuția...")
    await asyncio.sleep(2)
    await ServiciuC()


async def ServiciuC():
    print("Serviciu C: Finalizarea secvenței.")
    await asyncio.sleep(1)


async def main():
    await ServiciuA()


if __name__ == "__main__":
    asyncio.run(main())
