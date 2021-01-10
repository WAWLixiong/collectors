#!/usr/bin/env python3
# coding:utf-8

class IGamePlayer:

    def get_proxy(self):
        raise NotImplementedError

    def login(self, user, password):
        raise NotImplementedError

    def kill_boss(self):
        raise NotImplementedError

    def upgrade(self):
        raise NotImplementedError


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


class GamePlayerProxy(IGamePlayer):

    def __init__(self, game_player):
        self.game_player = game_player

    def get_proxy(self):
        return self

    def kill_boss(self):
        self.game_player.kill_boss()

    def login(self, user, password):
        self.game_player.login(user, password)

    def upgrade(self):
        self.game_player.upgrade()

class Client_1:
    """直接实例化用户"""

    def run(self):
        player = GamePlayer('张三')
        player.login('张三', 'lixiong')
        player.kill_boss()
        player.upgrade()

class Client_2:
    """直接实例化代理类"""

    def run(self):
        player = GamePlayer('张三')
        proxy = GamePlayerProxy(player)
        proxy.login('张三', '李雄')
        proxy.kill_boss()
        proxy.upgrade()

class Client:
    """通过用户获取代理"""

    def run(self):
        player = GamePlayer('张三')
        proxy = player.get_proxy()
        proxy.login('张三', '李雄')
        proxy.kill_boss()
        proxy.upgrade()


if __name__ == '__main__':
    # client_1 = Client_1()
    # client_1.run()
    # client_2 = Client_2()
    # client_2.run()
    client = Client()
    client.run()

