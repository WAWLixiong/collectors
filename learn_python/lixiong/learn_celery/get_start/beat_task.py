#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 上午 10:08:42
# @Author  : zzlion
# @File    : beat_task.py
# @Reference: celery-mannual:125

from learn_python.lixiong.learn_celery.get_start.tasks import app, add
from celery.schedules import crontab


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls add('hello') every 10 seconds.
    sender.add_periodic_task(10.0, add.s(1, 2), name='add every 10')
    # Calls add('world') every 30 seconds
    sender.add_periodic_task(30.0, add.s(3, 4), expires=10)
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        add.s(5, 6),
    )


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'learn_python.lixiong.learn_celery.get_start.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'add-every-monday-morning': {
        'task': 'learn_python.lixiong.learn_celery.get_start.tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (30, 30),
    },
}
app.conf.timezone = 'UTC'
