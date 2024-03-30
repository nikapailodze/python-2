import time
import threading
start = time.perf_counter()
listt = []
def sleeep(sec):
    print('sleepin', sec, 'seconds')
    time.sleep(sec)
    print('finished!')
number=threading.active_count()
print (number)
for i in range(number):
    t = threading.Thread(target = sleeep, args=[5])
    t.start()
    listt.append(t)
for i in listt:
    i.join()

finish = time.perf_counter()
print(round((finish-start),2))