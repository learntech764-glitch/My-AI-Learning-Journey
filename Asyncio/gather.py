import asyncio

async def cook(name, time):
    await asyncio.sleep(time)
    return f"{name} ready in {time}s"

async def main():
    results = await asyncio.gather(
        cook("Pizza A", 2),
        cook("Pizza B", 3)
    )
    print(results)

asyncio.run(main())
