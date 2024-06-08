import threading
import time


def producer():
    print("Searching for a book")
    time.sleep(1)
    print("Book found")
    event.set()
    ###
    event.clear()


def consumer():
    print("Waiting for a book")
    event.wait()
    print("Book is Exists")


event = threading.Event()

thread_1 = threading.Thread(target=producer)
thread_2 = threading.Thread(target=consumer)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
