#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 下午 05:49:39
# @Author  : zzlion
# @File    : test_condition.py
# @Reference:

import threading
import time


class Client:
    lock = threading.Lock()
    condition = threading.Condition()
    interval = 6
    check_condition = threading.Condition()

    def __init__(self):
        self.buffer = []
        self.last_time = time.time()

    def check(self):
        with self.check_condition:
            while True:
                self.check_condition.wait()
                if time.time() - self.last_time > self.interval:


    def consumer(self):
        with self.condition:
            while True:
                self.condition.wait()
                print('i am consumer: consumer:{} length, last: {}'.format(
                    len(self.buffer), self.buffer[-1]
                ))
                self.buffer.clear()
                self.condition.notify()

    def producer(self):
        with self.condition:
            for i in range(10000):
                self.buffer.append(i)
                self.last_time = time.time()
                # 在buffer满了, 或者buffer未满，但是现在的时间 与 last_time超过了 interval
                if len(self.buffer) == 300:
                    print('producer transform')
                    self.condition.notify()
                    self.condition.wait()
                self.check_condition.notify()
                self.check_condition.wait()

    def run(self):
        th1 = threading.Thread(target=self.producer)
        th2 = threading.Thread(target=self.consumer)
        th2.start()
        th1.start()

if __name__ == '__main__':
    client = Client()
    client.run()
