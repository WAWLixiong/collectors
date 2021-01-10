#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 上午 10:02:22
# @Author  : zzlion
# @File    : test_get_magic.py
# @Reference:

class A:

    def __init__(self):
        self.name = 'zz'

    def method1(self):
        print('hi')

    @staticmethod
    def method2():
        pass

    @classmethod
    def method3(cls):
        pass

    suggen = {'zz': method1}
    def main_method(self):
        a = self.suggen[self.name]
        b = a.__get__(self)
        print(a)
        print(b)
        b()
        a(self)


if __name__ == '__main__':
    a = A()
    # print(A.main_method)
    # print(A.method1)
    # print(A.method2)
    # print(A.method3)
    # print(a.main_method)
    a.main_method()