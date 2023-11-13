import asyncio


async def ServiciuA():
    print("Serviciu A: Execuția...")
    await asyncio.sleep(1)
    return "Rezultat din Serviciu A"


async def ServiciuB():
    print("Serviciu B: Execuția...")
    await asyncio.sleep(3)
    return "Rezultat din Serviciu B"


async def Orchestrator():
    print("Orchestrator: Inițierea orchestrării...")

    resultA = await ServiciuA()
    resultB = await ServiciuB()

    final_result = f"Rezultatele sunt: {resultA}, {resultB}"

    print(f"Orchestrator: Finalizarea orchestrării. {final_result}")


async def main():
    await Orchestrator()


if __name__ == "__main__":
    asyncio.run(main())
