#!/usr/bin/env python3
# coding:utf-8

from learn_python.lixiong.learn_design_pattern.learn_proxy_pattern import GamePlayer

class InvocationHandler:
    """JDK提供的动态代理接口"""


class GamePlayIH(InvocationHandler):
    # 被代理者
    cls = None
    # 被代理的实例
    obj = None
    # 我要代理谁
    def __init__(self, obj):
        self.obj = obj

    # invoke方法是接口InvocationHandler定义必须实现的，他完成对真实方法的调用
    # 动态代理是根据被代理的接口生成所有的方法,
    # 默认情况下所有的方法的返回值都是空的
    def invoke(self, proxy, method, object, *args, **kwargs):
        result = method.invoke(self.obj, *args, **kwargs)
        return result


class Client:

    def run(self):
        player = GamePlayer('张三')
        # 定义一个handler
        invocation_handler = GamePlayIH(player)
        print('开始时间是：2020-01-02 09:29:32')
        invocation_handler
