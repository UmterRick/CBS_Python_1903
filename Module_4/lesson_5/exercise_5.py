import threading
import time


def producer():
    print(f"{threading.current_thread().name}: Set locking ")

    time.sleep(1)
    with lock:
        print(f"{threading.current_thread().name}: Done")
        with lock:
            print(f"{threading.current_thread().name}: Nice")
    print(f"{threading.current_thread().name}: Release Lock")


lock = threading.RLock()  # Lock()

thread_1 = threading.Thread(target=producer)
thread_2 = threading.Thread(target=producer)

print('Thread-1 Start')
thread_1.start()
print('Thread-2 Start')
thread_2.start()

thread_1.join()
thread_2.join()
