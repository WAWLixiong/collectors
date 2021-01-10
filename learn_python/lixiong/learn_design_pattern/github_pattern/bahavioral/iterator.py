#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 02:41:18
# @Author  : zzlion
# @File    : iterator.py
# @Reference:

def count_to(count):
    numbers = ['one', 'two', 'three', 'four', 'five']
    yield from numbers[: count]

count_to_two = lambda : count_to(2)
count_to_five = lambda : count_to(5)

def main():
    for number in count_to_two():
        print(number)

    for number in count_to_five():
        print(number)


if __name__ == '__main__':
    main()