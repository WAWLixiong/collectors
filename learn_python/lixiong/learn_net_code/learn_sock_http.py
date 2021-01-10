import socket
from urllib.parse import urlparse


def get_url(url):
    #通过sock请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,80))
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    html_data = data.decode('utf8').split('\r\n\r\n')[1]
    print(html_data)
    client.close()

get_url('http://www.baidu.com')
