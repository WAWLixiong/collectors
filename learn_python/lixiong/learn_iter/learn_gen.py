from collections.abc import Iterator

def fun():
    yield 1
    yield 2
    yield 3
#为延迟求值，提供了可能


def fun2():
    return 1

def fib(index):
    if index < 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n<index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list


def fib3(index):
    n, a, b = 0, 0, 1
    while n<index:
        yield b
        a, b = b, a+b
        n += 1





if __name__ == '__main__':
    #生成器对象在python编译字节码的时候就产生了
    a = fun()
    b = fun2()
    print(type(a))
    print(type(b))
    print(isinstance(a,Iterator)) #True

    print(next(a))
    print(next(a))
    print(next(a))

    # print(fib(40))
    print(fib2(10))

    for i in fib3(10):
        print(i)
