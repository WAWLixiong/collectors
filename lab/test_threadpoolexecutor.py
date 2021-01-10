#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 上午 10:17:36
# @Author  : zzlion
# @File    : test_threadpoolexecutor.py
# @Reference:

from concurrent.futures import ThreadPoolExecutor, as_completed, ALL_COMPLETED, wait
import time

server = ThreadPoolExecutor()
li = []
future_list = []

def test():
    li.append(1)
    return 'hi'

for i in range(1, 100000):
    future = server.submit(test)
    future_list.append(future)


wait(future_list, return_when=ALL_COMPLETED)
print(len(li))


