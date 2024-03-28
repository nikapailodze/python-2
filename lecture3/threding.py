import threading
import time


# done = False

# def worker():
#     counter=0
#     while not done:
#         time.sleep(1)
#         counter+=1
#         print(counter)

# threading.Thread(target=worker).start()
# # worker()



# input("Press enter to quit")

# done=True






# print(threading.active_count()) #one thread running our program
# print(threading.enumerate()) #MainThread in charge of main program




def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")
def dring_coffe():
    time.sleep(4)
    print("you drink coffee")

def study():
    time.sleep(5)
    print("you finished studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=dring_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# eat_breakfast()
# dring_coffe()
# study()







