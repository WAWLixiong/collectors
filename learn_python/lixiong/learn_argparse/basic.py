#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午 04:26:43
# @Author  : zzlion
# @File    : basic.py
# @Reference:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, choices=[1, 2, 3])
group = parser.add_mutually_exclusive_group()
# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
# group.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)
group.add_argument("-v", "--verbose",  action="store_true")
group.add_argument("-q", "--quite", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
