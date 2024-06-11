import asyncio
import time

import aiohttp
import requests

all_urls = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
    'https://github.com',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/1',
]


async def fetch_url(url):
    async with aiohttp.request("get", url) as request:
        return url, await request.text()


async def async_main():
    tasks = [
        asyncio.ensure_future(fetch_url(url)) for url in all_urls
    ]
    start_time = time.time()
    for future in asyncio.as_completed(tasks):
        url, text = await future
        print(url)
    print(f"Async complete in {time.time() - start_time}")


def sync_main():
    start_time = time.time()
    for url in all_urls:
        requests.get(url)
        print(url)
    print(f"Sync complete in {time.time() - start_time}")


sync_main()
time.sleep(2)
print()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(async_main())
