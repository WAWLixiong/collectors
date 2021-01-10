import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # AF_INET = 2 相当于IPv4
    # AF_INET6 = 23 相当于IPv6
    # AF_UNIX  进程间通讯


    # SOCK_DGRAM = 2 UDP协议
    # SOCK_STREAM = 1 TCP协议

server.bind(('0.0.0.0', 8000))
server.listen()
soc,add = server.accept()

#获取从客户端发送的数据
#一次获取1k的大小
data = soc.recv(1024)
print(data.decode('utf8'))
soc.send("hi,i am fine".encode('utf8'))

server.close()
soc.close()
