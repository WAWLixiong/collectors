#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 下午 06:36:16
# @Author  : zzlion
# @File    : test_config.py
# @Reference:

import logging
from lab.logging_server_and_client.load_log_config import load_config

load_config()


a = logging.getLogger('a')
a_b = logging.getLogger('a.b')
a_c = logging.getLogger('a.c')

a.handle()

a.info('hello')
a.debug('china')
a_b.error('world')
a_c.error('never')
