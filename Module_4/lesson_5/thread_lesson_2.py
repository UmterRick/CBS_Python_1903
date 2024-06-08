import threading
import time


def task(start: int = 0, finish: int = 0):
    # print("Task executing in thread")
    result = 0
    for i in range(start, finish):
        result += i
    results.append(result)


results = []
# print("Create thread")
thread_1 = threading.Thread(target=task, kwargs={"finish": 2 ** 12})
thread_2 = threading.Thread(target=task, kwargs={"start": 2 ** 12, "finish": 2 ** 24})
# print("Start thread")
start_time = time.time()
thread_1.start()
thread_2.start()
# print("Thread Started")

thread_1.join()
thread_2.join()
print(results)
print('RESULTS 1')
print("Time = ", time.time() - start_time)
print('Value: ', sum(results))

print("\n\n")

results = []
started_at = time.time()
task(finish=2 ** 24)
print('RESULTS 2')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))