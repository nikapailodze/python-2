import datetime
import time
import threading
day=datetime.date(2024,4,3)
print(day.weekday()==5)

start=time.perf_counter()

def dosmt(sec):
    print(f"sleep for {sec}")
    time.sleep(sec)
    print("done")




t1=threading.Thread(target=dosmt,args=[3])
t2=threading.Thread(target=dosmt,args=[4])
t1.start()
t2.start()
t1.join()
t2.join()

end=time.perf_counter()


print(f"final {round(end-start,2)}")