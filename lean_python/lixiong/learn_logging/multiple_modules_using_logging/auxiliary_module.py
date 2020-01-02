#!/usr/bin/env python3
# coding:utf-8


import logging

logger = logging.getLogger('main_module.auxiliary_module')

class Auxiliary:

    def __init__(self):
        self.logger = logging.getLogger('main_module.auxiliary_module.Auxiliary')
        self.logger.info('creating an instancce of auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    logger.info('received a call to some_function')
