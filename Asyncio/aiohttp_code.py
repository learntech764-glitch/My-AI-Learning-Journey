import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url} -> {response.status}")

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://api.github.com"
    ]
    tasks = [asyncio.create_task(fetch(u)) for u in urls]

    print("Requests started...")
    for t in tasks:
        await t   # wait for each task

asyncio.run(main())
