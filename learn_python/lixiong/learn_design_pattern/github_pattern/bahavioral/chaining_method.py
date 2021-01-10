#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 12:52:19
# @Author  : zzlion
# @File    : chaining_method.py
# @Reference:


class Person:

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action


class Action:
    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')


def main():
    move = Action('move')
    person = Person('Jack', move)
    person.do_action().amount('5m').stop()


if __name__ == '__main__':

    main()
