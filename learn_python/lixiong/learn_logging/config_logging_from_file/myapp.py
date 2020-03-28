#!/usr/bin/env python3
# coding:utf-8

import logging
from learn_python.lixiong.learn_logging.config_logging_from_file import mylib


def main():
    filename = '/var/log/collectors/collectors/example.log'
    logging.basicConfig(filename=filename, filemode='w', level=logging.DEBUG)
    logging.info('start')
    mylib.do_something()
    logging.info('finshed')

if __name__ == '__main__':
    main()