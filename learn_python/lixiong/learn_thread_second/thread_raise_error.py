import threading
import time

def fun1():
    time.sleep(2)
    return 1 + 2

def fun2():
    time.sleep(1)
    raise NotImplementedError()

th_list = []
th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)
th_list.append(th1)
th_list.append(th2)

for th in th_list:
    th.start()

for th in th_list:
    th.join()


print('main thread no error')