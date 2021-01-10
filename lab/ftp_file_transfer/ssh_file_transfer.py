#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 下午 10:40:25
# @Author  : zzlion
# @File    : ssh_file_transfer.py
# @Reference:

import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
filename = r'E:\projects\collectors\pylint.conf'
remot_path = '/usr/local/src/pylint.conf'
ssh.connect('47.96.156.199', username='root', password='sqfh512.~')
sftp = ssh.open_sftp()
# sftp.mkdir('/home/zzlion/projects/test_ftp')
sftp.put(filename, remot_path, callback=None)
ssh.close()
#
# with open(filename, 'r') as f:
#     content = f.readline()
#     print(content)