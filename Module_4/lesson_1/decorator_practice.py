import time

def catch_time_outer(time_measurement):
    def catch_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            exec_time = time.time() - start_time
            if time_measurement == "ms":
                exec_time *= 1000
            elif time_measurement == "s":
                pass
            print(f"Catch Time: Function {func.__name__} was executed in {exec_time} {time_measurement}")

            return result
        return wrapper
    return catch_time

@catch_time_outer("ms")
def some_test_func(a, b, c):
    time.sleep(3)
    return a * b ** c

@catch_time_outer("s")
def func_2():
    time.sleep(2)
    return 10

x = some_test_func(2, 3, 4)
print(x)

y = func_2()
print(y)