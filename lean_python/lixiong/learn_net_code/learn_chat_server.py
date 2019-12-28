import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('0.0.0.0', 8000))
server.listen(128)

def handle_sock(soc, addr):
    while True:
        data = soc.recv(1024)
        print(data.decode('utf8'))
        message = input('please input:')
        soc.send("{}".format(message).encode('utf8'))


while True:
    soc,add = server.accept()
    th = threading.Thread(target=handle_sock, args=(soc, add))
    th.start()

