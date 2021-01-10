#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 上午 11:54:58
# @Author  : zzlion
# @File    : __init__.py.py
# @Reference:

# from loguru import logger

import logging

logging.basicConfig(format='[%(asctime)-15s] [%(levelname)s]\t - %(message)s\t (%(filename)s:%(lineno)s)\t hello world')
logger = logging.getLogger(__name__)

# formatter = logging.Formatter('[%(asctime)-15s] [%(levelname)s] - %(message)s (%(filename)s:%(lineno)s)')
# handler = logging.StreamHandler()
# logger.addHandler(handler)
# logger.addFilter(formatter)

logger.setLevel(logging.INFO)

logger.info('start flask app')
logger.error('hello world')
logger.warning('i am tired because i am not happy')
logger.critical('you are a da ben dan')
