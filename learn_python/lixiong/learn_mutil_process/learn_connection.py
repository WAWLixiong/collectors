import time
from multiprocessing import Process
# from queue import Queue
#用于进程间通讯的专用Queue
#共享全局变量不能用于多进程，
#multiprocessing中的Queue不能用于ProcessPoolExecutor
from multiprocessing import Queue
from multiprocessing import Pool
from multiprocessing import Manager
from multiprocessing import Pipe

# def producer(queue):
#     queue.put('a')
#     print('put')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)


# if __name__ == '__main__':
#     # queue = Queue(10)
#     # pro1 = Process(target=producer, args=(queue,))
#     # pro2 = Process(target=consumer, args=(queue,))
#     # pro1.start()
#     # pro2.start()
#     # pro1.join()
#     # pro2.join()
#
#     #进程池中的通讯要用Manager中的Queue
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#     pool.close()
#     pool.join()



# def producer(pipe):
#     pipe.send('a')
#     print('put')
#     time.sleep(2)
#
#
# def consumer(pipe):
#     time.sleep(2)
#     data = pipe.recv()
#     print(data)
#
#
# #通过pipe实现进程间通讯
# if __name__ == '__main__':
#     receive_pipe, send_pipe = Pipe()
#     #pipe只能用于两个进程
#     #pipe性能高于queue，由于queue有锁的机制
#     pro1 = Process(target=producer, args=(send_pipe,))
#     pro2 = Process(target=consumer, args=(receive_pipe,))
#     pro1.start()
#     pro2.start()
#     pro1.join()
#     pro2.join()

def add_data(p_dict, key, value):
     p_dict[key] = value

if __name__ == '__main__':
     # 通过共享内存的方式通讯
     # python常见的内置类型在Manager中都可以看见
     # 共享内存的时候需要主要 使用Lock，Rlock同步数据
     progress_dict = Manager().dict()
     first_progress = Process(target=add_data, args=(progress_dict, 'name','zzlion'))
     second_progress = Process(target=add_data, args=(progress_dict, 'age','18'))
     first_progress.start()
     second_progress.start()
     first_progress.join()
     second_progress.join()
     print(progress_dict)




