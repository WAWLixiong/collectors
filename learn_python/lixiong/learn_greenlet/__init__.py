#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 下午 10:43:31
# @Author  : zzlion
# @File    : __init__.py.py
# @Reference:


from greenlet import greenlet
import time

def test1():
    while True:
        print('hi')
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print('world')
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
