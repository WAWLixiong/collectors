# 什么是协程，即可以暂停的函数，可以往暂停的地方传入值


def gen_fun():
    #这行代码的作用
    # 1 产出值，2 接收值(调用方传递进来的值)
    html = yield 'http://www.baidu.com'
    print(html)
    yield 2
    yield 3
    return 4


if __name__ == '__main__':
    gen = gen_fun()
    html = 'zzlion'
    #send方法启动生成器，程序进程到下一个yield方法处
    # 并传递值到赋值语句的右边
    html = gen.send(None)
    value = gen.send(html)
    print(html)
    print(value)

