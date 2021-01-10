#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 上午 09:23:54
# @Author  : zzlion
# @File    : test_class_decorator.py
# @Reference:


class A:

    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        print('in A')
        return self.method(*args, **kwargs)


class B:

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print('in B')
            return self.method(*args, **kwargs)
        return wrapper


class C:
    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        print('in C')
        return self.method(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print('in C')
            return self.method(*args, **kwargs)
        return wrapper


class Client:

    @A
    def test1(self):  # test1 <==> A(test1)
        print('test1')

    @B
    def test2(self):  # test2 <==> B(test2)
        print('test2')

    @C
    def test3(self):
        print('test3')


class Test:

    def __get__(self, instance, owner):
        print('hi world')


if __name__ == '__main__':
    client = Client()
    # 两个类中的wrapper居然在内存中只有一个
    print(client.test1)  # <__main__.A object at 0x7f4b59f200f0>
    print(client.test2)  # <function B.__get__.<locals>.wrapper at 0x7f1b5f77be18>
    print(client.test3)  # <function C.__get__.<locals>.wrapper at 0x7f1b5f77be18>

    # test = Test()
