#__getattr__ 在找不到属性的时候回进入此魔法方法，可以用于实现，大小写，动态获取不存在的属性值
# __getattribute__所有的属性查找都会进入这个方法，尽量不要重写这个方法

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