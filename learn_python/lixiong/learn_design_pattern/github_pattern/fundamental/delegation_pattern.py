#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 下午 11:38:26
# @Author  : zzlion
# @File    : delegation_pattern.py
# @Reference:

from __future__ import annotations
from typing import Any, Callable, Union

class Delegator:

    def __init__(self, delegate: Delegate):
        self.delegate = delegate

    def __getattr__(self, name: str) -> Union[Any, Callable]:
        attr = getattr(self.delegate, name)
        if not callable(attr):
            return attr
        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)
        return wrapper


class Delegate:
    def __init__(self):
        self.p1 = 123

    def do_something(self, something: str) -> str:
        return f"Doing{something}"
