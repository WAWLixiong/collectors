#!/usr/bin/env python3
# coding:utf-8

from __future__ import absolute_import, unicode_literals
from celery import Celery


mq_user = 'zzlion'
mq_password = 'lixiong6660'
mq_host = '47.96.156.169'
mq_port = '5672'
mq_virtual_host = '/'

proj_name = 'proj'
broker = 'amqp://{}:{}@{}:{}/{}'.format(mq_user, mq_password, mq_host, mq_port, mq_virtual_host)
backend = broker
include = ['project.tasks']

app = Celery('proj', broker=broker, backend=backend, include=include)

app.conf.update(result_expires=3600)


if __name__ == '__main__':
    app.start()