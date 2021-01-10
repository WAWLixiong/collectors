# 引起死锁的原因：A(a,b)
# import dis
#Rlock 在同一个线程内可以多次调用lock.acquire, 但是acquire的次数必须和release的次数相同
from threading import Thread, Lock, RLock

def add(a):
    a += 1


def sub(a):
    a -= 1


"""
1. load a
2. load 1
3. +/-
4. 赋值给a
"""

# print(dis.dis(add))
# print(dis.dis(sub))

num = 0
lock = RLock()

def fun1():
    global num
    global lock
    lock.acquire()
    lock.acquire()
    for i in range(1000000):
        num += 1
    lock.release()
    lock.release()


def fun2():
    global num
    global lock
    lock.acquire()
    for i in range(1000000):
        num -= 1
    lock.release()


if __name__ == '__main__':
    th1 = Thread(target=fun1)
    th2 = Thread(target=fun2)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(num)
