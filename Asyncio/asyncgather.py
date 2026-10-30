import asyncio
import time

async def fetch_data(name):
    print(f"Fetching data for {name}...")
    await asyncio.sleep(2)  # Simulate a delay in fetching data
    print(f"Data fetched for {name}.") 
    return f"Data for {name} fetched."

async def main():
    results= await asyncio.gather(
        fetch_data("users"),
        fetch_data("orders"),
        fetch_data("products")
    )
    print(results)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
