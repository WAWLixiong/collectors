#!/usr/bin/env python3
# coding:utf-8

# caution 有N个产品族，在抽象工厂类中就有N个创建方法, e.g. 左前门--左前门把手--左前门窗户，
# caution 有M个产品等级就应该有M个实现工厂类，在每个实现工厂中，实现不同产品族的生产任务
#  e.g. 车前门(门的各种配件)，车前轮胎(前轮的各种配件)
from abc import abstractmethod


class AbstractProductA:

    def share_method(self):
        """
        每个产品线共有的方法
        """

    @abstractmethod
    def do_something(self):
        """
        每个产品线共有方法，不同实现
        """


class ProductA1(AbstractProductA):

    def do_something(self):
        return 'product_a1'


class ProductA2(AbstractProductA):

    def do_something(self):
        return 'product_a2'


class AbstractProductB:

    def share_method(self):
        """
        B产品线共有的方法
        """

    def do_something(self):
        """
        每个产品线共有的方法，不同的实现
        """


class ProductB1(AbstractProductB):

    def do_something(self):
        return 'product_b1'


class ProductB2(AbstractProductB):

    def do_something(self):
        return 'product_b2'


class AbstractCreactor:

    @abstractmethod
    def create_product_a(self):
        """
        创建A产品
        """

    @abstractmethod
    def create_product_b(self):
        """
        创建B产品
        """


class Creactor1(AbstractCreactor):
    """
    创建产品1
    """

    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class Creactor2(AbstractCreactor):
    """
    创建产品2
    """

    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


class Client:

    def execute(self):
        creator1 = Creactor1()
        creator2 = Creactor2()

        a1 = creator1.create_product_a()
        b2 = creator1.create_product_b()

        a2 = creator2.create_product_a()
        b2 = creator2.create_product_b()
