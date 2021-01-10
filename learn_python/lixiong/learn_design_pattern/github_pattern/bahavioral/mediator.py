#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 03:28:51
# @Author  : zzlion
# @File    : mediator.py
# @Reference:

class ChatRoom:
    """Mediator class"""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User:
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')

    molly.say("Hi Team! Meeting at 3PM today")
    mark.say("Roger that!")
    ethan.say("Alright.")

if __name__ == '__main__':
    main()
