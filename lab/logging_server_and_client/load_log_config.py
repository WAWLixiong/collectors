#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 下午 06:10:50
# @Author  : zzlion
# @File    : load_log_config.py
# @Reference:

import logging.config
import json


def load_config():
    with open('/home/zzlion/projects/collectors/logging.json') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
