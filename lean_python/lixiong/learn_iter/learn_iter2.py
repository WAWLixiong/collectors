#for循环，首先找出iter方法，没有在查找getitem方法
class MyCompany:
    def __init__(self,company):
        self.company = company

    def __iter__(self):
        return MyIter(self.company)

    # def __getitem__(self, item):
    #     return self.company[item]

class MyIter:
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
    for item in myiter:
        print(item)
