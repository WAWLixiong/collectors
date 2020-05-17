#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午 09:30:16
# @Author  : zzlion
# @File    : test_event.py
# @Reference:

import threading
import time
event = threading.Event()

a = []

def produce():
    for i in range(30):
        a.append(i)
        print('append {}'.format(i))
        time.sleep(0.1)
        if len(a) == 20:
            event.set()
        if len(a) == 30:
            event.clear()

def comsumer():
    print('i am wait a singal')
    event.wait()
    for i in range(10):
        time.sleep(0.1)
        print(a[-1], end=', ')
    event.wait()
    print('this cant appear')

th_list = []
th1 = threading.Thread(target=produce)
th2 = threading.Thread(target=comsumer)

th_list.append(th1)
th_list.append(th2)
for t in th_list:
    t.start()
for t in th_list:
    t.join()
print(a[-1])
print(len(a))
