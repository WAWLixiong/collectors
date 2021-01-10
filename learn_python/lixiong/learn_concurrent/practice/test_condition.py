#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午 10:51:40
# @Author  : zzlion
# @File    : test_condition.py
# @Reference:

from threading import Condition, Thread
import time

cv = Condition()
cake_status = False

def make_cake():
    print('i am making a cake')
    time.sleep(5)
    print('make a cake')
    global cake_status
    cake_status = True
    return 'cake'

def cost_cake():
    print('cost for the cake')
    return 'ok'

# Consumer
def consumer():
    with cv:
        while not cake_status:
            print('i wait hungry')
            cv.wait()
        cost_cake()

# Producer
def producer():
    with cv:
        make_cake()
        cv.notify()

th = []
t1 = Thread(target=consumer, name='consumer')
t2 = Thread(target=producer, name='producer')
th.append(t1)
th.append(t2)

for t in th:
    # caution: 这里不能join
    t.start()
