def gen_func():
    try:
        yield 'hello'
    except Exception as e:
        pass
    yield 1
    yield 2
    return 3


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, 'download error')
    print(next(gen)) # yield 2没有进行吗？
    # gen.throw(Exception, 'hhh')
    # print(next(gen))
