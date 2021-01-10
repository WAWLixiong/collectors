#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 下午 02:23:31
# @Author  : zzlion
# @File    : command.py
# @Reference:

class HideFileCommand:

    def __init__(self):
        self._hidden_files = []

    def execute(self, filename):
        print(f'hiding{filename}')
        self._hidden_files.append(filename)

    def undo(self):
        filename = self._hidden_files.pop()
        print(f'un-hiding {filename}')


class DeleteFileCommand:

    def __init__(self):
        self._deleted_files = []

    def execute(self, filename):
        print(f'deleting {filename}')
        self._deleted_files.append(filename)

    def undo(self):
        filename = self._deleted_files.pop()
        print(f'restoring {filename}')


class MenuItem:

    def __init__(self, command):
        self._command = command

    def on_do_press(self, filename):
        self._command.execute(filename)

    def on_undo_press(self):
        self._command.undo()


def main():
    item1 = MenuItem(DeleteFileCommand())
    item2 = MenuItem(HideFileCommand())
    test_file_name = 'test-file'

    item1.on_do_press(test_file_name)
    item1.on_undo_press()

    item2.on_do_press(test_file_name)
    item2.on_undo_press()


if __name__ == '__main__':
    main()