#比较简单的的话直接调用threading.Thread()
#复杂情况下就需要继承Thread类


import threading
import time

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print("get detail url")
        time.sleep(4)
        print("get detail url end")

if __name__ == '__main__':
    thread1 = GetDetailHtml('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')

    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("end time spend {}".format(time.time() - start_time))
