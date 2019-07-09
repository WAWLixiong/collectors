#Future未来对象，submit的时候返回Future对象
from concurrent.futures import Future, ThreadPoolExecutor

#未来对象，task的返回容器
# Future的设计理念，在线程，进程，协程的设计中是相通的

def fun1(time):
    print(1)



executor = ThreadPoolExecutor(max_workers=5)

task1 = executor.submit(fun1,(1))

