#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 上午 12:34:30
# @Author  : zzlion
# @File    : data_and_no_data_descriptor.py
# @Reference:

import numbers

class IntField:
    """ 实现任意一个下列方法都是属性描述符 """
    # 实现了 __get__ 与 __set__ 为数据描述符

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataStrField:
    # 只实现了__get__为非数据描述符

    def __get__(self, instance, owner):
        return "non data"

class User:
    age = IntField()
    school = 'jingsheng'
    nondata = NonDataStrField()

if __name__ == '__main__':
    user = User()
    user.age = 19
    # -----------------------------------------
    # 数据描述符会进入类的__dict__当中, 不会进入实例的__dict__
    print(User.__dict__) # {'__module__': '__main__', 'age': <__main__.IntField object at 0x7f64e10e6828>, 'school': 'jingsheng', 'nondata': <__main__.NonDataStrField object at 0x7f64d9c02898>, '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None}
    print(user.__dict__) # {}

    # -----------------------------------------
    # 数据描述符的查找最高，然后查找实例的属性，最后是类的
    # 非数据描述符
    user.__dict__['age'] = 20
    print(user.age)
    print(user.nondata) # "non data"
    user.__dict__['nondata'] = "fine"
    print(User.__dict__) # {'__module__': '__main__', 'age': <__main__.IntField object at 0x7fafb476b828>, 'school': 'jingsheng', 'nondata': <__main__.NonDataStrField object at 0x7fafad288898>, '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None}
    print(user.__dict__) # {'age': 20, 'nondata': 'fine'}
    print(user.nondata) # fine