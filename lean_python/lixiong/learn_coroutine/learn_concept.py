# 什么是协程，即可以暂停的函数，可以往暂停的地方传入值
# 采用同步的方式去编写异步的代码
# 使用单线程的方式去切换任务
# 1线程是由操作系统切换的，单线程切换意味着我们需要程序员自己调度任务
# 2不在需要锁，并发性能高，如果单线程内切换函数，性能远高于线程切换，并发性高


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

