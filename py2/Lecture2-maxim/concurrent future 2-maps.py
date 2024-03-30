import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print('sleeping', seconds, 'seconds')
    time.sleep(seconds)
    return 'Done Sleeping...'+str(seconds)


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    
print (results)

    
finish = time.perf_counter()

print('Finished in', round(finish-start, 2), 'second(s)')