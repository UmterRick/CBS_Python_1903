import asyncio
import random
import time


# async / await
async def async_worker(number, divider):
    sleep_value = random.randint(1, 5)
    print(f"Async Worker with {number=} and {divider=} (sleep={sleep_value})")
    await asyncio.sleep(sleep_value)

    result = number / divider
    print(result)
    return result


async def gather_worker():
    results = await asyncio.gather(
        async_worker(100, 10),
        async_worker(1000, 125),
        async_worker(500, 125),
        async_worker(567860, 125),
        async_worker(1000, 15),
        async_worker(1080, 20),
    )
    print(results)


start_time = time.time()
event_loop = asyncio.get_event_loop()
tasks = [
    event_loop.create_task(gather_worker())

]

main_task = asyncio.wait(tasks)
event_loop.run_until_complete(main_task)
event_loop.close()
