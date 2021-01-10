#__getattr__ 在找不到属性的时候回进入此魔法方法(i.e. 可以找到属性时不进入此方法)，
# __getattribute__所有的属性查找都会进入这个方法(i.e. 在这个方法下调用self.属性，会重新进入这个方法，导致递归)，尽量不要重写这个方法

from datetime import date

class User:
    def __init__(self, name, age, info=None):
        self.name = name
        self.age = age
        self.info = info

    def __getattr__(self, item):
        # return '{} not found'.format(item)
        return self.info[item]

    def __getattribute__(self, item):
        return 'bobby'



if __name__ == '__main__':
    user = User('zz','0313',info={'height':175})
    print(user.height)
    # user.__getattribute__('birthday')
    # print(user.__getattr__('age'))
    # print(user.getattr('age'))
    print(getattr(user, 'age'))