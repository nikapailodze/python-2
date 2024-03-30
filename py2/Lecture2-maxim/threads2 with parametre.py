import time
import threading

start = time.perf_counter()

threads = []

def do_something(seconds):
    print('sleeping', seconds, 'seconds')
    time.sleep(seconds)
    return 'Done Sleeping...}'

for i in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
    

finish = time.perf_counter()

print('Finished in', round(finish-start, 2), 'second(s)')