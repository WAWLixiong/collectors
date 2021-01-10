#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午 09:14:51
# @Author  : zzlion
# @File    : threading_test.py
# @Reference:

import threading
import time

a = threading.current_thread()
b = threading.get_ident()

def fun():
    c = 1 + 3
    time.sleep(0.4)
    print(c)
    return c
th = []
for i in range(3):
    t = threading.Thread(target=fun)
    th.append(t)

for t in th:
    t.setDaemon(True)
    t.start()

c = threading.enumerate()
d = threading.TIMEOUT_MAX
print('end')
