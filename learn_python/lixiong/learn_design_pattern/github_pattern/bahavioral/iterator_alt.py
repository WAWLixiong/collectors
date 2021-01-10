#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 02:45:07
# @Author  : zzlion
# @File    : iterator_alt.py
# @Reference:


class NumberWords:
    _WORD_MAP = (
        'one', 'two', 'three', 'fout', 'five',
    )

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self): # this makes the class an Iterable
        return self

    def __next__(self): # this makes the class an Iterator
        if self.start > self.stop or self.start > len(self._WORD_MAP):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


def main():
    a = NumberWords(start=1, stop=2)
    print(iter(a))
    print(type(iter(a)))
    print(isinstance(a, Iterator))
    for number in a:
        print(number)

    for number in NumberWords(start=1, stop=5):
        print(number)


if __name__ == '__main__':
    from collections import Iterable, Iterator
    # class A:
    #     def __iter__(self):
    #         return self
    #
    # a = A()
    # iter(a)
    # print(isinstance(a, Iterable))
    main()
