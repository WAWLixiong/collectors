#gil使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行
#gil会根据执行的字节码长度 或一定时间后 或io操作时 释放锁，所以才会造成以下数据混乱


# import dis
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

import threading


total = 0

def add():
    global total
    for i in range(100000):
        total += 1

def desc():
    global total
    for i in range(100000):
        total -= 1


th1 = threading.Thread(target=add)
th2 = threading.Thread(target=desc)

th1.start()
th2.start()
th1.join()
th2.join()
print(total)
