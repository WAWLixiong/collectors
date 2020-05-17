#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午 10:09:37
# @Author  : zzlion
# @File    : lock_test.py
# @Reference:

import threading
import time

lock = threading.Lock()

def fun():
    with lock:
        time.sleep(2)
        ret = 3
        print(ret)
        return ret

th = threading.Thread(target=fun)
th.start()
print(2)
l = lock.acquire(blocking=False)
print(l)
time.sleep(4)
l = lock.acquire(blocking=False)
print(l)