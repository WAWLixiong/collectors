#实现了iter方法就是可迭代类型
#
from collections.abc import Iterator, Iterable

class MyIter(Iterator):

    def __init__(self,name):
        self.name = name

    def __next__(self):
        return self.name


if __name__ == '__main__':
    myiter = MyIter(name='zzlion')

    a = [1,2]
    b = iter(a)
    print(isinstance(a,Iterator)) #False
    print(isinstance(a,Iterable)) #True
    print(isinstance(b,Iterator)) #True
