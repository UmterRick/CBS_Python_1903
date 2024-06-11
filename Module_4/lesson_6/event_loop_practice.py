import asyncio


async def async_worker(seconds):
    print(f"Start AsyncWorker with {seconds}")
    await asyncio.sleep(seconds)
    print(f"Done Sleep {seconds} seconds")


async def stop_event_loop(loop, seconds):
    print(f"Stop in {seconds} seconds")
    await asyncio.sleep(seconds)
    loop.stop()
    print("Loop stopped")


async def resolve_future(fut: asyncio.Future):
    await asyncio.sleep(5)
    print("Set future value to -----")
    # fut.set_result(20)


async def wait_for_future(fut: asyncio.Future):
    result = await fut
    print("Future result: ", result)

event_loop = asyncio.get_event_loop()

my_future = asyncio.Future()

event_loop.create_task(async_worker(3))
event_loop.create_task(async_worker(2))

event_loop.create_task(stop_event_loop(event_loop, 20))
event_loop.create_task(wait_for_future(my_future))
event_loop.create_task(resolve_future(my_future))
event_loop.run_forever()
event_loop.close()
