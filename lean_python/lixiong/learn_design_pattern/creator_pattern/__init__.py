#!/usr/bin/env python3
# coding:utf-8

from abc import abstractmethod


class AbstractCarBuilder:

    @abstractmethod
    def set_queue(self, queue):
        pass

    @abstractmethod
    def get_carmodel(self):
        pass


class AbstractCarModel:

    def __init__(self):
        self.queue = None


    @abstractmethod
    def alarm(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def set_queue(self, queue):
        self.queue = queue

    def run(self):
        for action in self.queue:
            if action == 'start':
                self.start()
            elif action == 'stop':
                self.stop()
            elif action == 'alarm':
                self.alarm()


class BenzModel(AbstractCarModel):

    def alarm(self):
        return 'benz alarm'

    def start(self):
        return 'benz start'

    def stop(self):
        return 'benz stop'


class BMWModel(AbstractCarModel):

    def alarm(self):
        return 'bmw alarm'

    def start(self):
        return 'bmw start'

    def stop(self):
        return 'bmw stop'


class BenzBuilder(AbstractCarBuilder):

    benz = BenzModel()

    def set_queue(self, queue):
        self.benz.set_queue(queue)

    def get_carmodel(self):
        return self.benz


class BMWBuilder(AbstractCarBuilder):

    bmw = BenzModel()

    def set_queue(self, queue):
        self.bmw.set_queue(queue)

    def get_carmodel(self):
        return self.bmw


class Client:
    """
    没有导演类的客户端
    """

    def execute(self):
        benz_builder = BenzBuilder()
        queue = []
        queue.append('start')
        queue.append('stop')
        queue.append('alarm')
        benz_builder.set_queue(queue)
        benz = benz_builder.get_carmodel()
        benz.run()


class Director:
    """
    导演类
    """

    def __init__(self):
        self.queue = []
        self.benz_builder = BenzBuilder()
        self.bmw_builder = BMWBuilder()

    def get_bmw_a(self):
        self.queue.clear()
        self.queue.append('stop')
        self.queue.append('start')
        self.bmw_builder.set_queue(self.queue)
        return self.bmw_builder.get_carmodel()

    def get_bmw_b(self):
        self.queue.clear()
        self.queue.append('alarm')
        self.queue.append('alarm')
        self.bmw_builder.set_queue(self.queue)
        return self.bmw_builder.get_carmodel()

    def get_benz_a(self):
        self.queue.clear()
        self.queue.append('alarm')
        self.queue.append('start')
        self.benz_builder.set_queue(self.queue)
        return self.benz_builder.get_carmodel()


class Client2:
    """
    有导演情况下的客户端
    """

    def execute(self):
        director = Director()

        for i in range(1000):
            director.get_bmw_a().run()

        for i in range(1000):
            director.get_bmw_b().run()

        for i in range(1000):
            director.get_benz_a().run()

if __name__ == '__main__':
    client = Client2()
    client.execute()

