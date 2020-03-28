#!/usr/bin/env python3
# coding:utf-8

import logging
from logging import LoggerAdapter
import random


class MyLoggerAdapter(LoggerAdapter):

    def process(self, msg, kwargs):
        return '[{}] {}'.format(self.extra['request_id'], msg), kwargs

class RequestIDGenerator:
    request_ids_pool = []

    def __init__(self):
        self.container = {}

    def __getitem__(self, item):
        return self.container[item]

    def __iter__(self):
        # 只用来表明自己是一个迭代器
        return self

    def __next__(self):
        it = iter(self.container)
        return next(it)



def main():
    logger = logging.getLogger(__name__)
    fh = logging.FileHandler('/var/log/projects/collectors/adapter.log')
    formatter = logging.Formatter('%(name)s %(asctime)s %(msg)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    adapter = MyLoggerAdapter(logger, {'request_id': '1912104128'})
    adapter.setLevel(logging.DEBUG)
    adapter.info('hi i am fine')

if __name__ == '__main__':
    main()
