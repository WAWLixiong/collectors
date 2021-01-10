#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午 10:34:37
# @Author  : zzlion
# @File    : test_queue.py
# @Reference:

import queue
import threading
import time

q = queue.Queue()

def producer():
    return range(30)

def do_work(item):
    print(item)
    time.sleep(0.2)

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

def manager():
    num_worker_threads = 6
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in producer():
        q.put(item)

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()