#多进程 可以利用多cpu并发的机制
#多进程与多线程的区别
#耗cpu操作的用多进程编程, 对于io操作用多线程编程
#多进程切换比多线程切换代价大
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

start_time = time.time()
with ThreadPoolExecutor(3) as executor:
    all_task = [executor.submit(fib,(i)) for i in range(25, 40)]
    for future in as_completed(all_task):
        data = future.result()
        print('exec result: {}'.format(data))
    print(time.time() - start_time)


#windows下使用多进程的话，一定要放在 if __name__ == '__main__': 下边

# if __name__ == '__main__':
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib,(i)) for i in range(25, 40)]
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print('exec result: {}'.format(data))
    #     print(time.time() - start_time)

