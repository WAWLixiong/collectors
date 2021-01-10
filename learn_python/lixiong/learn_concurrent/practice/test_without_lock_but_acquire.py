#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午 06:37:04
# @Author  : zzlion
# @File    : test_without_lock_but_acquire.py
# @Reference:

from threading import Thread, Lock

lock = Lock()
a = lock.acquire()
print(a)