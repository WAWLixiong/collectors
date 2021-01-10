#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 上午 10:02:53
# @Author  : zzlion
# @File    : instance.py
# @Reference:


class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            # instance.__dict__[self.storage_name] = value # 不能setattr，否则还会触发__set__, 造成递归
            setattr(instance, self.storage_name, value) # 这里的storage_name已经与托管实例不是一个名字了
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    lineitem = LineItem('desc', 10, 13)
    print(lineitem.weight)
    print(lineitem.price)
    lineitem.weight = 13
    print(lineitem.weight)
    print(lineitem.price)

    print(LineItem.weight)

