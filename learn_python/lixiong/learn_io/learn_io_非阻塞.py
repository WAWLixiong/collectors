import socket
from urllib.parse import urlparse


#非阻塞io，但是下一步依赖上一步，这种情况下并没有提高我们的并发

def get_url(url):
    #通过sock请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host,80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
            break
        except BlockingIOError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
            if d:
                data += d
            else:
                break
        except BlockingIOError as e:
            continue
    html_data = data.decode('utf8').split('\r\n\r\n')[1]
    print(html_data)
    client.close()

get_url('http://www.baidu.com')
