#for循环，首先找出iter方法，没有在查找getitem方法
#迭代器不支持切片

from collections.abc import Iterator


#注意定义一个可迭代对象的时候一定不要直接在里边实现迭代器，而是应该单独实现一个迭代器，在可迭代对象中返回迭代器

class MyCompany:
    def __init__(self,company):
        self.company = company

    def __iter__(self):
        #__iter__方法必须返回iterator
        return MyIter(self.company)

    # def __getitem__(self, item):
    #     return self.company[item]

class MyIter(Iterator):
    """自定义一个迭代器"""
    def __init__(self, employ_list):
        self.employ_list = employ_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值得逻辑
        try:
            work_staff = self.employ_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return work_staff


if __name__ == '__main__':
    myiter = MyCompany(['a', 'b', 'c'])
    # print(next(myiter))
    print(isinstance(myiter, Iterator))
    print(isinstance(MyIter, Iterator))
    # for item in myiter:
    #     print(item)
