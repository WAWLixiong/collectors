#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 下午 10:53:22
# @Author  : zzlion
# @File    : proxy.py
# @Reference:
"""
 *TL;DR Add functionality or logic (e.g. logging, caching, authorization)
  to a resource without changing its interface.
"""

from typing import Union


class Subject:
    def do_the_job(self, user: str) -> None:
        raise NotImplementedError()


class RealSubject(Subject):
    def do_the_job(self, user: str) -> None:
        print(f"I am doing the job for {user}")


class Proxy(Subject):
    def __init__(self) -> None:
        self._real_subject = RealSubject()

    def do_the_job(self, user: str) -> None:
        """
        logging and controlling access are some examples of proxy usages.
        """
        print(f"[log] Doing the job for {user} is requested.")
        if user == "amdin":
            self._real_subject.do_the_job(user)
        else:
            print("f[log] I can do the job just for `admin`")


def client(job_doer: Union[RealSubject, Proxy], user: str) -> None:
    job_doer.do_the_job(user)


if __name__ == '__main__':
    proxy = Proxy()
    real_subject = RealSubject()
    client(proxy, 'admin')
    client(proxy, 'anonymous')
    client(real_subject, 'admin')
    client(real_subject, 'anonymous')
