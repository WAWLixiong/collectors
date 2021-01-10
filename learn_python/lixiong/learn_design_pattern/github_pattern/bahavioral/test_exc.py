#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 上午 09:10:36
# @Author  : zzlion
# @File    : test_exc.py
# @Reference:

import sys
import traceback


def main():
    try:
        1 / 0
    except Exception as e:
        err_type, err_value, err_trace = sys.exc_info()
        # print(err_type)
        # print(err_value)
        # print(err_trace)
        a = traceback.format_exception(err_type, err_value, err_trace)
        print(''.join(a))



if __name__ == '__main__':
    main()