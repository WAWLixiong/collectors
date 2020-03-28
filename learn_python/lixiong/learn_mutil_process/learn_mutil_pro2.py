import time
# import os
#
# #fork只能用于linux/unix下边，不能用于windows下边
# # fork会创造一个子进程
# # fork的子进程会将父进程的代码原样copy，包括运行
# # 父进程运行结束就退出,如果子进程还没有结束，就不会结束
# pid = os.fork()
# print('zzlion')
# if pid == 0:
#     print('子进程 {} 父进程 {}'.format(os.getpid(), os.getppid()))
# else:
#     print('我是父进程：{}'.format(pid))
# time.sleep(2)


#multiprocessing 更加底层
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

#多进程编程
def get_html(n):
    time.sleep(n)
    print('sub_progress success')
    return n

if __name__ == '__main__':
    # process = multiprocessing.Process(target=get_html, args=(2,))
    # print(process.pid)
    # process.start()
    # print(process.pid)
    # process.join()
    # print(process.pid)
    # print('main progress end')
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) #amd的2600居然显示为12
    # result = pool.apply_async(get_html,args=(3,))  #返回值类似于Future
    # pool.close()
    #在调用join之前， 一定要先调用close方法
    # pool.join()
    # print(result.get())

    #使用下边这种方式，不需要pool的close，join方法调用
    # for result in pool.imap(get_html, [1,5,3]):
    #     print(result)

    #谁先完成把谁打印出来
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print(result)



