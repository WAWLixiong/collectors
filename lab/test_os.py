#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 下午 09:01:38
# @Author  : zzlion
# @File    : test_os.py
# @Reference:

import time

from memory_profiler import profile

@profile
def fun():
    file_handler = open('test_lixiong', 'w')

    count = 0
    while True:
        time.sleep(1)
        file_handler.write('hello{}\n'.format(count))
        if count % 6 == 0:
            file_handler.flush()
        if count == 60:
            file_handler.close()
            break
        count += 1


if __name__ == '__main__':
    fun()

