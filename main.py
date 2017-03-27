# -*- coding: UTF-8 -*-

import sys


def list_avaliable():
    print 'test'

commands = [
    {'name': 'list', 'func': list_avaliable},
]

if __name__ == '__main__':
    func = commands[0].get('func')
    if func:
        func()
    