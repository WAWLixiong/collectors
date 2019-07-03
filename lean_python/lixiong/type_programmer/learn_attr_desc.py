#只要类里边实现任意一个一下魔法函数，即为属性描述符  __get__ __set__ __delete__
#通过这种方式控制传输属性的类型
#数据描述符 与 非数据描述符 查找顺序是不一致的
import numbers

"""
如果user是某个类的实例，那么user.age等价于 getattr(user,'age')
首先调用__getattribute__。如果类定义了__getattr__方法，那么在__getattribute__方法报 AttributeError的时候，
就会调用__getattr__方法，
而对于__get__的调用，则是发生在__getattribute__内部的。

user = User(), 那么user.age的顺序如下：
1)如果'age' 是出现在User或者基类的__dict__中，且age是data descriptor,那么调用其__get__方法（优先级最高),否则
2）如果'age'出现在user的__dict__中，那么直接返回obj.__dict__['age'],否则
3）如果'age'出现在User或者基类的__dict__中（即不是属性描述符）
3.1）如果age是non-data descriptor ,那么调用__get__方法，否则
3.2）返回__dict__['age']
4）如果User有__getattr__方法，调用__getattr__方法，否则
5）抛出AttributeError
"""

class IntField:
    """实现了__get__,__set__是一种数据描述符"""
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value
        pass

    def __delete__(self, instance):
        pass

class NonDataIntField:
    """非数据描述符"""
    def __get__(self, instance, owner):
        return self.value



class User:
    age = IntField()
    # age = NonDataIntField()

if __name__ == '__main__':
    user = User()
    # user.age = 30 #赋值会进入__set__方法
    user.__dict__['age'] = 'abc'
    print(user.__dict__) #数据描述符的话为空，即赋值不会进入实例的属性，而是进入属性描述符中 #非数据描述符的话则是作为对象的属性
    print(user.age) # 如果没有user.age = 30 进行赋值的话 会报错 AttributeError: 'IntField' object has no attribute 'value'
