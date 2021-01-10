# ⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⡅⡅⠄⠄⠄⠄⡉⠹⠄⡅⠄⠄⠄
# ⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀
# ⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿
# ⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿
# ⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉
# ⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇
# ⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿
# ⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾
# ⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃
# ⠛⢿⣿⣿⣿⣦⠁⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄
# ⠄⠄⠉⠻⣿⣿⣿⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀
# ⣮⣥⠄⠄⠄⠛⢿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿

#回调之痛
#阅读困难
#共享变量困难，需要作为实例变量
#异常处理困难

import socket
from urllib.parse import urlparse
# import select
# select.select(rlist, wlist, xlist, timeout=None)

#selector 是在select的基础上包装的更加好用
# DefaultSelector会根据平台自动选择是poll还是epoll
# 提供了一种注册的机制
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()
urls = ['http://www.baidu.com'] * 20
stop = False

# 使用select完成http请求
class Fetcher:

    def connected(self, key):
        #回调函数中要取消注册的事件
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # #回调函数中要取消注册的事件
        # selector.unregister(key.fd)
        d = self.client.recv(1024)
        #编程readable之后，不代表可以一直从内核空间复制数据到用户空间
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            html_data = self.data.decode('utf8').split('\r\n\r\n')[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            global stop
            if not urls:
                stop = True

    def get_url(self, url):
        self.spider_url = url
        self.data = b''
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host,80))
        except BlockingIOError as e:
            pass

        #注册，将socket注册到selector中
        # fileobj, events, data=None
        # 文件对象，事件， 回调函数


        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


#回调需要自己调用
#事件循环，虽然写了回调函数，但是不是在其可调用的时候，系统自动帮我们调用，而是需要我们手动控制回调
def loop():
    #事件循环，不停的请求socket的状态并调用对应的回调函数（twisted，tarndo，gevent，协程，asyncio）
    #回调+事件循环+select(poll/epoll)

    # 1.
    # select 本身是不支持register模式的
    # selector 对 select封装后，支持register模式，

    # 2.
    # socket状态变化以后的回调是由程序员完成的
    # key的数据类型，进入register方法查看源代码，SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])
    while not stop:
        ready = selector.select() # 这个地方在windows下会报错(设置一个全局变量，请求的url结束以后，退出循环则不会报错)，
        # linux下epoll不会报错
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls:
        feacher = Fetcher()
        feacher.get_url(url)
    loop()
    print(time.time() - start)


