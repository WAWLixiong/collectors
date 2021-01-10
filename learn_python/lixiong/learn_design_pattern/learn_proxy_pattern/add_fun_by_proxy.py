#!/usr/bin/env python3
# coding:utf-8
from learn_python.lixiong.learn_design_pattern.learn_proxy_pattern import (
    IGamePlayer,
)


class GamePlayer(IGamePlayer):
    proxy = None

    def __init__(self, name, ):
        self.name = name

    def get_proxy(self):
        self.proxy = GamePlayerProxy(self)
        return self.proxy

    def kill_boss(self):
        if self.proxy:
            print('{}在打怪'.format(self.name))
        else:
            print('请使用指定的代理访问')

    def login(self, user, password):
        if self.proxy:
            print('登录名为:{}'.format(user), '登录成功')
        else:
            print('请使用指定的代理访问')

    def upgrade(self):
        if self.proxy:
            print('{} 又升了一级'.format(self.name))
        else:
            print('请使用指定的代理访问')

    def is_proxy(self):
        if self.proxy is None:
            return False
        return True

class IProxy:

    def count(self):
        raise NotImplementedError


class  GamePlayerProxy(IGamePlayer, IProxy):

    def __init__(self, game_player):
        self.game_player = game_player

    def kill_boss(self):
        self.game_player.kill_boss()

    def login(self, user, password):
        self.game_player.login(user, password)

    def upgrade(self):
        self.game_player.upgrade()
        self.count()

    def count(self):
        print('总费用是340磅')

class Client:
    """通过proxy增加新功能，有点类似装饰器的作用"""

    def run(self):
        game_player = GamePlayer('张三')
        proxy = game_player.get_proxy()
        proxy.login('张三', '李雄')
        proxy.kill_boss()
        proxy.upgrade()

if __name__ == '__main__':
    client = Client()
    client.run()






