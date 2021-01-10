#!/usr/bin/env python3
# coding:utf-8

from .main import app


@app.route('/goods')
def goods():
    return 'goods'