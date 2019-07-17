import socket
from urllib.parse import urlparse
# import select
# select.select(rlist, wlist, xlist, timeout=None)

#selector 是在select的基础上包装的更加好用
# DefaultSelector会根据平台自动选择是poll还是epoll
# 提供了一种注册的机制
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()

# 使用select完成http请求
class Fetcher:

    def connected(self, key):
        #回调函数中要取消注册的事件
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, )

    def readable(self, key):
        #回调函数中要取消注册的事件
        selector.unregister(key.fd)
        data = b""
        while True:
            try:
                d = self.client.recv(1024)
                if d:
                    data += d
                else:
                    break
            except BlockingIOError as e:
                continue
        html_data = data.decode('utf8').split('\r\n\r\n')[1]
        print(html_data)
        self.client.close()

    def get_url(self, url):
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
    # 1.
    # select 本身是不支持register模式的
    # selector 对 select封装后，支持register模式，

    # 2.
    # socket状态变化以后的回调是由程序员完成的
    # key的数据类型，进入register方法查看源代码，SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])
    while True:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == '__main__':
    feacher = Fetcher()
    feacher.get_url('http://www.baidu.com')


