import threading
import time


def producer():
    with lock:
        print(f"{threading.current_thread().name}: Set locking - {lock._value}")
        print(f"{threading.current_thread().name}: Release - {lock._value}")

max_active_workers = 5
lock = threading.BoundedSemaphore(value=max_active_workers)

thread_1 = threading.Thread(target=producer)
thread_2 = threading.Thread(target=producer)
thread_3 = threading.Thread(target=producer)
thread_4 = threading.Thread(target=producer)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()


threads = []
for i in range(0, 1000):
    thread = threading.Thread(target=producer)
    threads.append(thread)

for i in threads:
    i.start()
