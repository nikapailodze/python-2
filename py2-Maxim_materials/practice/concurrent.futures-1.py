import concurrent.futures
import time

start =time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1 )
    # f2 = executor.submit(do_something,1 )
    # print(f1.result())
    # print(f2.result())

    secs = [5, 4, 3, 2, 1]
    results=[executor.submit(do_something,sec ) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    







# threads=[]

# for _ in range(10):
#     t =threading.Thread(target=do_something , args=[1.5])
#     t.start()
#     threads.append(t)


# for thread in threads:
#     thread.join()

finish=time.perf_counter()


print(f'finished in {round(finish-start, 2)} seconds')

