#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 下午 12:28:40
# @Author  : zzlion
# @File    : vistor.py
# @Reference: *TL;DR Separates an algorithm from an object structure on which it operates.


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break
        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit {}'.format(node.__class__.__name__))

    def visit_B(self, node, *args, **kwargs_):
        print('visit_B {}'.format(node.__class__.__name__))


def main():
    a, b, c = A(), B(), C()
    visitor = Visitor()

    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)


if __name__ == '__main__':
    main()
