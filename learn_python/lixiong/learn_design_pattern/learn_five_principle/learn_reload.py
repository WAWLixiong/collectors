#!/usr/bin/env python3
# coding:utf-8

# caution python 没有重载的说法
class Father:

    def get_value(self, field_map:dict):
        print('this is father')
        return list(field_map.values())

class Child(Father):

    def get_value(self, field_map:list):
        print('this is child')
        return list(field_map)


class Client:

    def invoker(self):
        # f = Father()
        # field_map = {'name':'1'}
        f = Child()
        field_map = [1,2]
        f.get_value(field_map)

if __name__ == '__main__':
    client = Client()
    client.invoker()


