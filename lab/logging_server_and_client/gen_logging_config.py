#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 下午 05:31:40
# @Author  : zzlion
# @File    : gen_logging_config.py
# @Reference:

import logging
import os


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        console_debug = os.getenv("CONSOLE_DEBUG")
        if console_debug in ('true', 'True', '1'):
            return False
        return True


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        console_debug = os.getenv("CONSOLE_DEBUG")
        if console_debug in ('true', 'True', '1'):
            return True
        return False


class NormalFilter(logging.Filter):
    def filter(self, record):
        file_debug = os.getenv("FILE_DEBUG")
        if file_debug in ('true', 'True', '1'):
            file_debug = True
        else:
            file_debug = False
        if record.levelno == logging.DEBUG:
            return file_debug
        return record.levelno <= logging.WARNING


class AbnormalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno > logging.WARNING
