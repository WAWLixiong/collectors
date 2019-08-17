# 在try，catch了GeneratorExit错误以后，什么也不做，只是pass，代码中还有yield的时候会报RunTimeError
# GeneratorExit 继承自BaseException，而不是Exception，BaseException是比Exception更基础的一个类
# gen.throw()也会让生成器往下走
def gen_fun():
    try:
        html = yield 'http://www.baidu.com'
        print(html)
    # except GeneratorExit:
    except Exception:
        pass
        # raise StopIteration
    yield 2
    yield 3
    yield 4
    return 5

if __name__ == '__main__':
    gen = gen_fun()
    print(gen.send(None))
    # gen.close()
    # next(gen) #StopIteration
    gen.throw(Exception, 'download error')
    print(next(gen))
    gen.throw(Exception, 'download error')
