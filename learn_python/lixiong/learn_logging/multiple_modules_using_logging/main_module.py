#!/usr/bin/env python3
# coding:utf-8

import logging
from learn_python.lixiong.learn_logging.multiple_modules_using_logging import auxiliary_module

logger = logging.getLogger('main_module')
logger.setLevel(logging.DEBUG)

## create file handler which logs even debug messages
fh = logging.FileHandler('multiple_modules.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# todo: 添加顺序是否会对logger的作用机制产生影响
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('called auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function')
auxiliary_module.some_function()
logger.info('called auxiliary_module.some_function')

# 日志输出
"""
2019-12-28 09:03:43,832 - main_module - INFO - creating an instance of auxiliary_module.Auxiliary
2019-12-28 09:03:43,832 - main_module.auxiliary_module.Auxiliary - INFO - creating an instancce of auxiliary
2019-12-28 09:03:43,832 - main_module - INFO - created an instance of auxiliary_module.Auxiliary
2019-12-28 09:03:43,832 - main_module - INFO - calling auxiliary_module.Auxiliary.do_something
2019-12-28 09:03:43,832 - main_module.auxiliary_module.Auxiliary - INFO - doing something
2019-12-28 09:03:43,832 - main_module.auxiliary_module.Auxiliary - INFO - done doing something
2019-12-28 09:03:43,832 - main_module - INFO - called auxiliary_module.Auxiliary.do_something
2019-12-28 09:03:43,832 - main_module - INFO - calling auxiliary_module.some_function
2019-12-28 09:03:43,832 - main_module.auxiliary_module - INFO - received a call to some_function
2019-12-28 09:03:43,832 - main_module - INFO - called auxiliary_module.some_function
"""
