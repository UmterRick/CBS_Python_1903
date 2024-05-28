import time
from functools import lru_cache

@lru_cache(maxsize=None)
def complicated_func(x):
    print("Calculate")
    time.sleep(1)
    return 100 + x


start_time = time.time()
print(complicated_func(1))
print(complicated_func(2))
print(complicated_func(3))
print(complicated_func(4))
print(complicated_func(1))
print(complicated_func(1))
print("END OF CODE")
print(time.time() - start_time, "seconds to execute")


# class Math:
#     @staticmethod
#     @lru_cache()
#     def calculate(x):