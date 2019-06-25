#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-24 07:29
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 3.单线程执行.py
# @Desc     :

from threading import current_thread

from gevent import monkey
monkey.patch_all()

import time
import gevent

def task(args):
    time.sleep(1)
    print(args)

def sync_func():  # 同步
    for i in range(10):
        task(i)


def async_func(): # 异步
    g_1= []
    for i in range(10):
        g_1.append(gevent.spawn(task,i))
    gevent.joinall(g_1)

start = time.time()
sync_func()
print(time.time()-start)

start = time.time()
async_func()
print(time.time()-start)

