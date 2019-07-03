#new 用来控制对象的生成过程，在对象生成之前
#init用来完善对象的
#如果new方法不返回对象，则不会调用init函数

class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self):
        print('in init')


if __name__ == '__main__':
    user = User()