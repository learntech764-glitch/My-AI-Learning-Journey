import asyncio

async def cook(name, time):
    await asyncio.sleep(time)
    print(f"{name} ready in {time}s")

async def main():
    task1 = asyncio.create_task(cook("Pizza A", 2))
    task2 = asyncio.create_task(cook("Pizza B", 3))

    print("Cooking started...")
    await task1   # wait for Pizza A
    await task2   # wait for Pizza B

asyncio.run(main())
