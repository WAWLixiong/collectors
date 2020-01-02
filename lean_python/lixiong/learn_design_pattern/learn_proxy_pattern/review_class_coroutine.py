#!/usr/bin/env python3
# coding:utf-8
import time


class A:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return '{}-{}'.format(self.name, self.age)

# a = A('lixiong', '19')
# a('hello', 'hi')
# ('hello', 'hi')
# {}


class Coroutine:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        start = time.time()
        obj = self.cls(*args, **kwargs)
        spend = time.time() - start
        print(obj)
        print(spend)
        return obj


@Coroutine
class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('{}-{}'.format(self.name, self.age))

    def __str__(self):
        return '{}-{}'.format(self.name, self.age)

"""
B --> Coroutine(B)
b = B() --> b = Coroutine(B)()
b.run()     
"""

if __name__ == '__main__':
    b = B('lixiong', '18')
