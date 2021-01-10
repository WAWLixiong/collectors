#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 下午 10:07:21
# @Author  : zzlion
# @File    : test_pformat.py
# @Reference:

from pprint import pformat, pprint

a = {
    'people': {
        'name': 'zzlion',
        'age': 18,
        'school': 20,
        'node': '232',
        'fad': 'dfasf'
    }
}
base = 'hi i am fine, how {}'.format(pformat(a))
print(a)
pprint(a)
print(base)