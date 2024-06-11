import asyncio


def some_big_func(value):
    result = 0
    for i in range(value**2):
        result += i
    return result


async def main(value):
    result = await loop.run_in_executor(None, some_big_func, value)
    print("Result = ", result)


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(main(10000)),
    loop.create_task(main(10003)),
])
loop.run_until_complete(tasks)
loop.close()