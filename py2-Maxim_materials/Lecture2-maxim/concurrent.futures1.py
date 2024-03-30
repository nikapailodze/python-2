import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print('sleeping', seconds, 'seconds')
    time.sleep(seconds)
    return 'Done Sleeping...'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1=executor.submit(do_something,5)
    f2=executor.submit(do_something,5)
    print (f1.result())
    print (f2.result())


finish = time.perf_counter()

print('Finished in', round(finish-start, 2), 'second(s)')