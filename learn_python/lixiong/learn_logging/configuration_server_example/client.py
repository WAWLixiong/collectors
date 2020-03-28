#!/usr/bin/env python3
# coding:utf-8

import socket
import sys
import struct


with open(sys.argv[1], 'rb') as f:
    data_to_send = f.read()

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting...')
s.connect((HOST, PORT))
print('sending config...')
pack = struct.pack('>L', len(data_to_send))
s.send(pack)
s.send(data_to_send)
s.close()
print('complete')
