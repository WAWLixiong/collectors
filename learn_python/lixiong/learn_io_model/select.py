#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 下午 10:44:03
# @Author  : zzlion
# @File    : select.py
# @Reference:

import socket
import select

ip_port = "0.0.0.0", 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ip_port)
server.listen(5)
server.setblocking(False)

inputs = [server]