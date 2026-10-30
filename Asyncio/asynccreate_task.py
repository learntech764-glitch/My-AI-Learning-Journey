import asyncio
import time

async def say_after(delay,message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello, world!"))
    task2 = asyncio.create_task(say_after(2, "Goodbye, world!"))

    await task1
    await task2

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
