#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-23 23:03
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : async.py
# @Desc     :


import queue
from functools import partial

eventlop = None
class EventLop(queue):
    def start(self):
        while True:
            function  =self.get()
            function()

def do_hello():
    global eventlop
    print(' hello')

    eventlop.put(do_hello)

def do_world():
    global eventlop
    print('world')

    eventlop.put(do_world)

if __name__ == '__main__':
    eventlop = EventLop()
    eventlop.put(do_hello)
    eventlop.start()