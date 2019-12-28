#线程间通讯的方式
#1）定义一个全局变量, 并不推荐这种方式，需要使用锁来确保线程安全
#2）通过queue的方式进行线程同步
import threading
import time
from lean_python.lixiong.learn_mutil_thread import test_variable_ken
# from lean_python.lixiong.learn_mutil_thread.test_variable_ken import deail_url_list

# detail_url_list = []
# detail_url_lsit = detail_url_lsit #这样会提示未定义
detail_url_list = test_variable_ken.deail_url_list

def get_detail_html(detail_url_list):
    # global detail_url_list
    while True:
        if detail_url_list:
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print('starting {}'.format(url))
            time.sleep(2)
            print('end')
        time.sleep(0.0001)

def get_detail_url(detail_url_list):
    # global detail_url_list
    while True:
        print('getting')
        time.sleep(3)
        for i in range(10):
            detail_url_list.append('http://www.bai.com/?page={}'.format(i))
        print('got')
        time.sleep(0.0001)

if __name__ == '__main__':
    th1 = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    th1.start()
    for i in range(10):
        th = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        th.start()

