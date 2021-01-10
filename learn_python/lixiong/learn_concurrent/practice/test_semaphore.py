#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午 09:05:46
# @Author  : zzlion
# @File    : test_semaphore.py
# @Reference:

import threading
import time
sem = threading.Semaphore(3)
class DemoThread(threading.Thread):
    def run(self):
        print('{0} is waiting semaphore.'.format(self.name))
        # sem.acquire()
        with sem:
            print('{0} acquired semaphore({1}).'.format(self.name, time.ctime()))
            time.sleep(5)
            print('{0} release semaphore.'.format(self.name))
        # sem.release()

if __name__ == '__main__':
    threads = []
    for i in range(4):
        threads.append(DemoThread(name='Thread-' + str(i)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()