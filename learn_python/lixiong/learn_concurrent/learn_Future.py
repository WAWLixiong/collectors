#Future未来对象，submit的时候返回Future对象
from concurrent.futures import Future, ThreadPoolExecutor

#未来对象，task的返回容器
# Future的设计理念，在线程，进程，协程的设计中是相通的

def fun1(time):
    print(1)



executor = ThreadPoolExecutor(max_workers=5)

task1 = executor.submit(fun1,(1))


# submit中有work_queue.put(work_item)
#submit紧接着调用adjust_thread_count的方法
#小于最大线程数，启动线程，target=_worker,args中有work_queue
#work_item中有run方法，调用了future.set_result(result)方法
#work_item=Work_item(f, fn, args, kwargs)


#看看Future中的方法
# cancel,取消任务，并设置状态
# canceled,设置状态
# running,设置状态
# 重要：result方法,由于condition方法是阻塞的，所有result也是阻塞的,阻塞的方法都会有timeout的

