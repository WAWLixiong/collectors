#!/usr/bin/env python3
# coding:utf-8

from types import MethodType

class InvocationHandler:
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print('handler', self.func, args, kwargs)
        print(self.func.__name__)
        return self.func(*args, **kwargs)

class HandlerException(Exception):

    def __init__(self, cls):
        super().__init__(cls, 'is not a handler class')


class Proxy:

    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = {}

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print('get attr', item)
        is_exists = hasattr(self.obj, item)
        res = None
        if is_exists:
            res = getattr(self.obj, item)
            if isinstance(res, MethodType):
                if self.handlers.get(res) is None:
                    self.handlers[res] = self.hcls(self.obj, res) # 返回sdk中 实际用户的方法，并做缓存
                return self.handlers[res]
            else:
                return res
        return res


class ProxyFactory:

    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise HandlerException(hcls)

    def __call__(self, cls):
        return Proxy(cls, self.hcls)


@ProxyFactory(InvocationHandler)
class Transaction:

    def __init__(self):
        pass

    def make_friend(self, a, b):
        print('hello', a ,b)

    def reply(self, a):
        print('hello', a)

if __name__ == '__main__':
    # learn: __getattr__ 在对象找不到的属性和方法时被调用
    """
    Transaction --> ProxyFactory(InvocationHandler)(Transaction)
    即调用了 ProxyFactory的__clall__方法, 返回Proxy(Transaction, InvocationHandler)对象 --> proxy
    
    tran = Transaction() --> proxy的__call__方法 为proxy对象添加了 obj = transaction 的属性, 并返回proxy对象
    
    tran.make_friend() --> proxy对象的 __getattr__, 会从sdk中回去该对象的
    
    """

    client = Transaction()
    client.make_friend('xiongming', 'xionghong')
