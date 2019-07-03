#类也是对象，type是创建类的类

def create_class(name):
    """动态创建类"""
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

#动态创建类,type获取某个对象的类型，type创建类

"""
type(object_or_name, bases, dict)
type(object) -> the object's type
type(name, bases, dict) -> a new type
# (copied from class doc)
"""
def say(self):
    return self.name

class Base:
    def answer(self):
        return 'i am baseclass'


#即使不继承，也需要填写一个空的元组
User_cls = type("User",(Base,),{'name':'user','say':say}) #元组内是继承的类，字典内是类的属性,

#元类是创建类的类，type就是一个元类

class Metaclass(type):
    """继承type则是元类"""
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class BaseClass(metaclass=Metaclass):
    pass


class User(BaseClass):
    """
    元类可以控制User实例化的过程,首先查找metaclass，通过metaclass创建User类，
    python中类的实例化过程
    type创建类对象,实例
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


if __name__ == '__main__':
    # Myclass = create_class("user")
    # my_obj = Myclass()
    # print(my_obj)
    my_obj = User_cls()
    print(my_obj)
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())

