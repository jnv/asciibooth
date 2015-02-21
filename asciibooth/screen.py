# -*- coding: utf-8 -*-
from blessings import Terminal

term = Terminal()

def status(message, clear=False, newline=True):
    if clear:
        print(term.clear() + term.move(0, 0))
    if newline:
        end = '\n'
    else:
        end = ' '
    print(message, end=end)

def output(lines, center=False):
    print(term.clear() + term.move(0, 0))
    print(lines)
