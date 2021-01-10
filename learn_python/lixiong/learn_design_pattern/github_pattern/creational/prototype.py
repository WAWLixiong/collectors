#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 下午 10:53:03
# @Author  : zzlion
# @File    : prototype.py
# @Reference:

class Prototype:

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispather:

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispather()
    prototype = Prototype()
    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)

    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    for key, p in dispatcher.get_objects().items():
        print({key: p.value})


if __name__ == '__main__':
    main()
