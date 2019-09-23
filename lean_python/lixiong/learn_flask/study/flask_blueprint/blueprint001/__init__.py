#!/usr/bin/env python3
# coding:utf-8


from flask import Blueprint

app_orders = Blueprint('app_orders', __name__, template_folder='templates') # static_url_path
# caution 蓝图需要指定templates路径, 小范围内没有会在项目路径中查找，
# caution 项目中的templates会覆盖蓝图目录中的templates中的


@app_orders.route('/')
def index():
    return 'hello world'

