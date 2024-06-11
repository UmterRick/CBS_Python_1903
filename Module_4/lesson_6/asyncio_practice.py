import asyncio
import time
from asyncio import iscoroutine


def sync_worker(number, divider):
    print(f"Sync Worker with {number=} and {divider=}")
    time.sleep(1)
    print(number / divider)


@asyncio.coroutine
def async_worker(number, divider):
    print(f"Async Worker with {number=} and {divider=}")
    yield from asyncio.sleep(3)
    print(number / divider)


@asyncio.coroutine
def async_worker_with_sync_sleep(number, divider):
    print(f"Async Worker with {number=} and {divider=}")
    time.sleep(5)
    print(number / divider)


# sync_worker(100, 10)
# async_worker(100, 10)

print("Sync ", iscoroutine(sync_worker))
print("Async", iscoroutine(async_worker(10, 2)))

start_time = time.time()
event_loop = asyncio.new_event_loop()
tasks = [
    event_loop.create_task(async_worker(100, 10)),
    event_loop.create_task(async_worker(1000, 125)),
    event_loop.create_task(async_worker(500, 125)),
    event_loop.create_task(async_worker(567860, 125)),
    event_loop.create_task(async_worker(1000, 15)),
    event_loop.create_task(async_worker(1080, 20)),
]

main_task = asyncio.wait(tasks)
event_loop.run_until_complete(main_task)
event_loop.close()

print(f"Completed in {time.time() - start_time}")

