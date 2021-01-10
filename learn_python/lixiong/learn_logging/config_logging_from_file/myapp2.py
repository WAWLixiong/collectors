#!/usr/bin/env python3
# coding:utf-8

import logging
# caution 所有的东西都会打印在console
# fmt = '%(levelname)s:%(message)s'
fmt = '%(asctime)s %(message)s' #  默认时间格式：ISO8601 or RFC 3339
# logging.basicConfig(format=fmt, level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')