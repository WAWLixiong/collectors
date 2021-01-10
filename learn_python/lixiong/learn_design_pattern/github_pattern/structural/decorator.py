#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 下午 10:22:19
# @Author  : zzlion
# @File    : decorator.py
# @Reference: *TL;DR Adds behaviour to object without affecting its class.


class TextTag:
    """Represents a base text tag"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}<b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = TextTag("hello world")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    print("before:", simple_hello.render())
    print("after:", special_hello.render())
