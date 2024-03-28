# import time

# start= time.perf_counter()

# def do_something():
#     print("Sleeping 5 seconds")
#     time.sleep(5)
#     return "Donne Sleeping"

# print(do_something())
# print(do_something())
# finish=time.perf_counter()

# print("Finished in", round(finish-start,2), "seconds(s)")



import time
import threading

start= time.perf_counter()

def do_something():
    print("Sleeping 5 seconds")
    time.sleep(5)
    return "Donne Sleeping"

t1=threading.Thread(target=do_something)
t2=threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()

print(do_something())
print(do_something())
finish=time.perf_counter()

print("Finished in", round(finish-start,2), "seconds(s)")


