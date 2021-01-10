#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 下午 09:18:32
# @Author  : zzlion
# @File    : __init__.py.py
# @Reference:

import signal
import os
import time

def handler(signum, frame):
    print("signal handler called with signal")
    # raise IOError("Could't open device")
    print("could't open device")


signal.signal(signal.SIGINT, handler)


def fun():
    while True:
        print('run')
        time.sleep(0.5)

if __name__ == '__main__':
    fun()
