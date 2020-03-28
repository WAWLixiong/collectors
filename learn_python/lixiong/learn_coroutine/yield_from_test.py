# yield from iterable

from itertools import chain

# chain将迭代的对象连接起来，直接一个for循环
my_list = [1, 2, 3]
my_dict = {'name': 'zzlion', 'age': 18}


# for value in chain(my_list, my_dict, range(5,10)):
#     print(value)

def my_chain(*args, **kwargs):
    for my_iter in args:
        yield from my_iter


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


def g1(iterable):
    yield range(10)


def g2(iterable):
    yield from range(10)


# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)
