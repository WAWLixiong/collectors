#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 上午 10:03:45
# @Author  : zzlion
# @File    : __init__.py.py
# @Reference:

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
    FIRST_COMPLETED,
)
import time

def get_html(i):
    # print('get html {}'.format(i))
    time.sleep(i)
    return i

def execute():
    executor = ThreadPoolExecutor(3)
    all_task = [executor.submit(get_html, i) for i in [0, 2, 3, 2, 6, 8]]
    for future in as_completed(all_task):
        yield future.result()

if __name__ == '__main__':
    for i in execute():
        print(i)

