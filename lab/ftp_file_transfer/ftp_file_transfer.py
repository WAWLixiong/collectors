#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 下午 10:15:34
# @Author  : zzlion
# @File    : ftp_file_transfer.py
# @Reference:


import ftplib
import re
import os
import sys
import socket


IPS = ['47.96.156.199']
USER_NAME = ['root']
PASSWORD = ['sqfh512.~']


def ftp_put_file():
    # ip =  '47.96.156.199'
    ip = 'www.zzlion.online'
    user_name = 'root'
    password = 'sqfh512.~'
    path = '/usr/local/src'
    bufsize = 1024
    try:
        f = ftplib.FTP(ip)
    except ftplib.error_perm:
        print('Error: cannot connect to {}'.format(ip))
        f.quit()
        return
    try:
        f.login(user_name, password)
    except (socket.error, socket.gaierror):
        print('Error: cannot login {}'.format(user_name))
        f.quit()
        return

    try:
        f.cwd(path)
    except ftplib.error_perm:
        print('Error: cannot cd to {}'.format(path))
        f.quit()
        return
    try:
        filename = 'pylint.conf'
        with open(filename, 'rb') as fi:
            f.storbinary('STOR {}'.format(filename), fi, bufsize)
    except ftplib.error_perm:
        print('Error: cannot read file {}'.format(filename))
    f.quit()
    return


if __name__ == '__main__':
    ftp_put_file()

