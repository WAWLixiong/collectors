import inspect
import re

class A:

    def __init__(self, name, age):
        self.dict = {'name': name, 'age': age}

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value

if __name__ == '__main__':
    a = '123'
    b = A('zzlion', 'age')
    ret = b['name']
    print(ret)
