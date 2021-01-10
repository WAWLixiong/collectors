#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 下午 05:05:57
# @Author  : zzlion
# @File    : test_srcfile.py
# @Reference:

import os

def fun():
    pass


print(os.path.normcase(fun.__code__.co_filename))
