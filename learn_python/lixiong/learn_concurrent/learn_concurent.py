#对于多线程编程，可以学习concurrent设计的管理模式，管理自己的线程


# 底层包，编写多进程，多线程变得异常容易，对这个包的理解，让我更容易理解协程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


# from concurrent import futures


# 线程池 什么情况下需要使用线程池
# 主线程中可以获取某一线程的状态或某一个任务的状态，以及返回值
# 当一个线程完成时，我们主线程能够立即知道
# futures这个包可以让多线程和多进程编码接口一致

def get_html(sleep_time):
    time.sleep(sleep_time)
    print('got page {} success '.format(sleep_time))
    return sleep_time


executor = ThreadPoolExecutor(max_workers=5)
# 通过submit方法提需要执行的任务到线程池, task1是一个future类, submit是非阻塞的，立即返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# done方法判断任务有没有完成
print(task1.done())
# cancel方法取消任务
# 已经开始的任务，无法取消，未开始的任务可以取消
print(task2.cancel())
time.sleep(3)
print(task1.done())

# result方法可以获取task的执行结果
print(task1.result())

# 获取已经成功的task的返回
urls = [4, 2, 5]
all_task = [executor.submit(get_html, (url)) for url in urls]

#wait方法等待特定的task执行完成后才往后执行
wait(all_task, return_when='FIRST_COMPLETED')
print("main")
for future in as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

#通过executor获取已经成功的task的返回
#map方法执行的结果顺序与任务的循序一致,而as_completed则是先执行性完的先打印
# for data in executor.map(get_html, urls):
#     print("get {} page success".format(data))

if __name__ == '__main__':
    pass
