#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 下午 12:20:11
# @Author  : zzlion
# @File    : define_queue.py
# @Reference:

from learn_python.lixiong.learn_celery.get_start.tasks import app, add, hello
from kombu import Queue

app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default', routing_key='task.#'),
    Queue('add', routing_key='zzlion.#'),
    Queue('hello', routing_key='zzlion.#'),
)
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.default'
