#!/usr/bin/env python3
# coding:utf-8

import logging
import logging.handlers
import os
import zlib


def namer(name):
    return name + '.gz'

def rotator(source, dest):
    with open(source, 'rb') as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, 'wb') as df:
            df.write(compressed)
    os.remove(source)


rh = logging.handlers.RotatingFileHandler('')
rh.rotator = rotator
rh.name = namer
