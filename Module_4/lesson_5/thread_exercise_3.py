import threading
param = list(range(0, 2**24))
thread = threading.Thread(target=sum, args=(param, ), name="My Named Thread")
# thread.start()
print(threading.active_count())
# thread.join()

curr_thread = threading.current_thread()
print(curr_thread)
print(curr_thread.daemon)
print(curr_thread.name)
print(thread.is_alive())
print(thread.name)



