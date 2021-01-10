#!/usr/bin/env python3
# coding:utf-8

from flask import Flask
from .goods import goods
from .blueprint001 import app_orders

app = Flask(__name__)

# app.register_blueprint(app_orders) #注册蓝图
app.register_blueprint(app_orders, url_prefix='/orders') #注册蓝图

# caution 解决循环引用的方式之一： 延迟引用，将需要应用的地方放在函数内部
# caution 将app装饰器的调用放在一个模块内
# caution 带参数的装饰器实际上是 函数的调用，深刻理解


app.route('/goods')(goods)
@app.route('/index')
def index():
    # from .goods import goods
    return 'welcome'


if __name__ == '__main__':
    app.run()