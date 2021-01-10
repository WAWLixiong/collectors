#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 上午 11:24:59
# @Author  : zzlion
# @File    : client.py
# @Reference:

import logging, logging.handlers
import time


rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)

socketHander = logging.handlers.SocketHandler(
'localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT
)
rootLogger.addHandler(socketHander)

logging.info('Jackdaws love my big sphinx of quartz')


logger1 = logging.getLogger("myapp.area1")
logger2 = logging.getLogger("myapp.area2")


logger1.debug("hello world")
time.sleep(3)
logger1.info("ni hao china")
time.sleep(3)

logger2.warning("how are you going")
time.sleep(3)
logger2.error("i am nice")
time.sleep(2)
