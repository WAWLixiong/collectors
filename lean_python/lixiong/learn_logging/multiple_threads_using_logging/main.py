#!/usr/bin/env python3
# coding:utf-8

import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('hi from my func')
        time.sleep(0.5)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False} # learn: 通过修改线程外部的参数值，线程内部的值也会变哈，这就是引用的原因
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()

    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join() # learn: 这个地方也值得学习，主线程到这个地方就要结束了，如果不能子线程，是不是子线程可能会成为孤儿？

if __name__ == '__main__':
    main()
