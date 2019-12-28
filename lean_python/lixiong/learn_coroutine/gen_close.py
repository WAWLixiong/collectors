# 在try，catch了GeneratorExit错误以后，什么也不做，只是pass，代码中还有yield的时候会报RunTimeError
# GeneratorExit 继承自BaseException，而不是Exception，BaseException是比Exception更基础的一个类
# gen.throw()也会让生成器往下走
def gen_fun():
    try:
        html = yield 'http://www.baidu.com'
        print(html)
    except GeneratorExit:
    # except Exception:
    #     pass
        raise StopIteration
    yield 2
    yield 3
    yield 4
    return 5

def gen_fun2():
    try:
        yield 'hello' # 第一次next会停在这一行，根本不会检测except
    except GeneratorExit as e:
        # pass # 直接pass会在gen.close()的地方报错
        raise StopIteration

    # except StopIteration as e:
    #     print('i am fine')
    yield 1
    yield 2

if __name__ == '__main__':
    # gen = gen_fun()
    # print(gen.send(None))
    # # gen.close()
    # # next(gen) #StopIteration
    # gen.throw(Exception, 'download error')
    # print(next(gen))
    # gen.throw(Exception, 'download error')

    gen = gen_fun2()
    print(next(gen))
    gen.close()
    next(gen)
