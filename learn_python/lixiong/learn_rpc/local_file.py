#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 下午 10:22:04
# @Author  : zzlion
# @File    : local_file.py
# @Reference:
import struct
from io import BytesIO


class InvalidOperation(Exception):
    def __init__(self, message):
        self.message = message

class MethodProtocol:

    def __init__(self, connection):
        self.conn = connection

    def _read_all(self, size):
        if isinstance(self.conn, BytesIO):
            buff = self.conn.read(size)
            return buff
        else:
            have = 0
            buff = b''
            while have < size:
                chunk = self.conn.recv(size - have)
                buff += chunk
                l = len(chunk)
                have += l
                if l == 0:
                    raise EOFError()
            return buff

    def get_method_name(self):
        buff = self._read_all(4)
        length = struct.unpack('!I', buff)[0]

        buff = self._read_all(length)
        name = buff.decode()
        return name



class DivideProtocol:

    def encode(self, num1, num2=1):
        name = 'divide'
        buff = struct.pack('!I', 6)
        buff += name.encode()

        buff2 = struct.pack('!B', 1)
        buff2 += struct.pack('!i', num1)

        if num2 != 1:
            buff2 += struct.pack('!B', 2)
            buff2 += struct.pack('!i', num2)

        buff += struct.pack('!I', len(buff2))
        buff += buff2
        return buff

    def _read_all(self, size):
        if isinstance(self.conn, BytesIO):
            buff = self.conn.read(size)
            return buff
        else:
            have = 0
            buff = b''
            while have < size:
                chunk = self.conn.recv(size - have)
                buff += chunk
                l = len(chunk)
                have += l
                if l == 0:
                    raise EOFError()
            return buff

    def decode(self, connection):
        param_len_map = {
            1: 4,
            2: 4
        }
        param_fmt_map = {
            1: '!i',
            2: '!i',
        }
        param_name_map = {
            1: 'num1',
            2: 'num2',
        }
        args = {}
        self.conn = connection
        buff = self._read_all(4)
        length = struct.unpack('!I', buff)[0]

        have = 0
        buff = self._read_all(1)
        have += 1
        param_seq = struct.unpack('!B', buff)[0]

        param_len = param_len_map[param_seq]
        buff = self._read_all(param_len)
        have += param_len
        param_fmt = param_fmt_map[param_seq]
        param = struct.unpack(param_fmt, buff)[0]

        param_name = param_name_map[param_seq]
        args[param_name] = param

        if have >= length:
            return args

        buff = self._read_all(1)
        param_seq = struct.unpack('!B', buff)[0]
        param_len = param_len_map[param_seq]
        buff = self._read_all(param_len)
        param_fmt = param_fmt_map[param_seq]
        param = struct.unpack(param_fmt, buff)[0]

        param_name = param_name_map[param_seq]
        args[param_name] = param
        return args

    def result_encode(self, result):
        if isinstance(result, float):
            buff = struct.pack('!B', 1)
            buff += struct.pack('!f', result)
        else:
            buff = struct.pack('!B', 2)
            length = len(result.message)
            buff += struct.pack('!I', length)
            buff += result.message.encode()

    def result_decode(self, connection):
        self.conn = connection
        buff = self._read_all(1)
        result_type = struct.unpack('!B', buff)

        if result_type == 1:
            buff = self._read_all(4)
            val = struct.unpack('!f', buff)[0]
            return val
        else:
            buff = self._read_all(4)
            length = struct.unpack('!I', buff)[0]
            buff = self._read_all(length)
            message = buff.decode()
            return message

if __name__ == '__main__':
    proto = DivideProtocol()
    # message = proto.encode(200, 100)
    message = proto.encode(200)
    conn = BytesIO()
    conn.write(message)
    conn.seek(0)

    method_proto = MethodProtocol(conn)
    method_name = method_proto.get_method_name()
    print(method_name)
    args = proto.decode(conn)
    print(args)