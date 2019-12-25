#!/usr/bin/env python3
# coding:utf-8

import logging

filename = '/var/log/collectors/collectors/example.log'

logging.basicConfig(filename=filename, filemode='w', level=logging.DEBUG) # level 可以是对应的数字
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('and this, too')
numeric_level = getattr(logging, 'INFO', None) # 20


# learn:level
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# learn:filemode
# 与文件的写入一致，w从头开始写入，a追加写入
