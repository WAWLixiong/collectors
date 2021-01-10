#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 10:24:49
# @Author  : zzlion
# @File    : test_property.py
# : https://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html


class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError('unreadable attribute')
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")

    def gettter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc


class A:

    @Property
    def name(self):
        return 'zz'


if __name__ == '__main__':
    a = A()
    print(a.name)

