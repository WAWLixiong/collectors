#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午 11:10:02
# @Author  : zzlion
# @File    : test_condition_graceful.py
# @Reference:

from threading import Condition, Thread
import time

cv = Condition()

def make_cake():
    print('i am making a cake')
    time.sleep(5)
    print('make a cake')
    return 'cake'

def cost_cake():
    print('cost for the cake')
    return 'ok'

def consumer():
    with cv:
        # while not cake_status:
        #     print('i wait hungry')
        #     cv.wait()
        print('i wait hungry')
        cv.wait_for(make_cake)
        cost_cake()
consumer()

