#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 上午 12:06:32
# @Author  : zzlion
# @File    : catalog.py
# @Reference:

class Catalog:

    def __init__(self, param):
        self._static_method_choices = {
            'param_value_1': self._static_method_1,
            'param_value_2': self._static_method_2,
        }
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print('executed method 1!')

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    def main_method(self):
        self._static_method_choices[self.param]()


class CatalogInstance:
    def __init__(self, param):
        self.x1 = 'x1'
        self.x2 = 'x2'
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {'param_value_1': _instance_method_1, 'param_value_2': _instance_method_2}

    def main_method(self):
        self._instance_method_choices[self.param].__get__(self)()

class CatalogClass:

    """catalog of multiple class methods that are executed depending on an init
    parameter
    """

    x1 = 'x1'
    x2 = 'x2'

    def __init__(self, param):
        # simple test to validate param value
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        print("Value {}".format(cls.x1))

    @classmethod
    def _class_method_2(cls):
        print("Value {}".format(cls.x2))

    _class_method_choices = {'param_value_1': _class_method_1, 'param_value_2': _class_method_2}

    def main_method(self):
        """will execute either _class_method_1 or _class_method_2
        depending on self.param value
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()

class CatalogStatic:

    """catalog of multiple static methods that are executed depending on an init
    parameter
    """

    def __init__(self, param):
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    _static_method_choices = {'param_value_1': _static_method_1, 'param_value_2': _static_method_2}

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2
        depending on self.param value
        """
        self._static_method_choices[self.param].__get__(None, self.__class__)()


if __name__ == '__main__':
    client = CatalogStatic('param_value_1')
    client.main_method()
