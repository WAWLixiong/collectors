#!/usr/bin/env python3
# coding:utf-8

import logging

fmt = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    format=fmt,
    datefmt='%m-%d %H:%M',
    filename='/var/log/projects/collectors/myapp.log',
    filemode='w'
)

# define a Handler which writes INFO messages or higher to the sys.sterr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format which is simple for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
console.setFormatter(formatter)
# learn: add the handler to the root logger
# todo:子类的logger没有handler 就会用父logger的handler, 所有的logger name都以 ''作为父logger
# todo:我们是不是可以将 root logger 的streamhandler 设置为error，这样就不用为子logger添加这个handler
# caution: 好像没有添加filehandler 也可以将日志输出到文件
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
# learn:可以直接使用logging打印日志
logging.info('Jackdaws love mye big sphinx of quartz.')

# application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

# 日志输出形式
"""
root        : INFO     Jackdaws love mye big sphinx of quartz.
myapp.area1 : INFO     How quickly daft jumping zebras vex.
myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.
myapp.area2 : ERROR    The five boxing wizards jump quickly.
"""