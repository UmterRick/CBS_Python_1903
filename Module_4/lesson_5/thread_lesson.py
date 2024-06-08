import threading  # thread - потік
import time


def task(start: int = 0, finish: int = 0):
    print("Task executing in thread")
    result = 0
    for i in range(start, finish):
        result += 1
    print("Value: ", result)


print("Create thread")
thread = threading.Thread(target=task, kwargs={"finish": 2 ** 25})
print("Start thread")
start_time = time.time()
thread.start()
print("Thread Started")

# thread.join()
print("Time = ", time.time() - start_time)
print("END OF PROGRAM")
