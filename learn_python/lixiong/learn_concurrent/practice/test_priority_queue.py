#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午 10:15:30
# @Author  : zzlion
# @File    : test_priority_queue.py
# @Reference:

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

a = PrioritizedItem(1, 'zzlion')
b = PrioritizedItem(2, 'lixong')
c = [b, a]
print(sorted(c))