#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 下午 10:48:21
# @Author  : zzlion
# @File    : __init__.py.py
# @Reference:

import gevent
from gevent import monkey
monkey.patch_all()
import time


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # gevent.sleep(0.4)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
# g1.join()
# g2.join()
# g3.join()

gevent.joinall([g1, g2, g3])