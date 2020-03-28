import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    message = input('please input')
    client.send('{}'.format(message).encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))



