#通过queue确保线程同步
#queue内部使用了dqueue， queue与deque都是线程安全的
# from collections import deque

import threading
import time
from queue import Queue
from learn_python.lixiong.learn_mutil_thread import test_variable_ken
# from learn_python.lixiong.learn_mutil_thread.test_variable_ken import deail_url_list

# detail_url_list = []
# detail_url_lsit = detail_url_lsit #这样会提示未定义
detail_url_list = test_variable_ken.deail_url_list

def get_detail_html(queue):
    # global detail_url_list
    while True:
        if queue:
            url = queue.get()
            # for url in detail_url_list:
            print('starting {}'.format(url))
            time.sleep(2)
            print('end')
        time.sleep(0.0001)

def get_detail_url(queue):
    # global detail_url_list
    while True:
        print('getting')
        time.sleep(3)
        for i in range(10):
            queue.put('http://www.bai.com/?page={}'.format(i))
        print('got')
        time.sleep(0.0001)

if __name__ == '__main__':
    queue = Queue(maxsize=5)
    th1 = threading.Thread(target=get_detail_url, args=(queue,))
    th1.start()
    for i in range(10):
        th = threading.Thread(target=get_detail_html, args=(queue,))
        th.start()
    #从queue的角度阻塞主线程，join一般与taskdone成对使用，只有调用了task_done阻塞的线程才会结束
    # queue.join()
    # queue.task_done()

