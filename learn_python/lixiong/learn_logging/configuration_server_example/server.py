#!/usr/bin/env python3
# coding:utf-8

import logging
import logging.config
import time
import os

# read initial config file
logging.config.fileConfig('logging.conf')

# create and start listener on port 9999
t = logging.config.listen(9999)
t.start()

logger = logging.getLogger('simpleExample')


try:
    # loop through logging calls to see the difference
    # new configurations make, until Ctrl + C is pressed
    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(5)
except KeyboardInterrupt:
    # cleanup
    logging.config.stopListening()
    t.join() # learn: 又遇到了相同的用法，在主线程快要退出的地方join
