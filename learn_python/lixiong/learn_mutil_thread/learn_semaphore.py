#semaphore(信号) 用于控制进入数量的锁
#文件一般允许一个线程写，多个线程读
#想要更确切的了解condition，可以看完queue的源码，像put阻塞的行为，就是利用了condition
import time
from threading import Semaphore
import threading
from queue import Queue

class HtmlSpider(threading.Thread):
    def __init__(self,url, sem):
        self.url = url
        self.sem = sem
        super().__init__()

    def run(self) -> None:
        time.sleep(2)
        print('got html')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider('http://baidu.com/?page={}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = Semaphore(3)
    urlproducer = UrlProducer(sem)
    urlproducer.start()



