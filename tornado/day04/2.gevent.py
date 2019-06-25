#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-24 07:17
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 2.gevent.py
# @Desc     :
from threading import current_thread

from gevent import monkey
monkey.patch_all()

import gevent

def fun1():
    print(current_thread().name)
    print('123')
    gevent.sleep(1)
    print('456')

def fun2():
    print(current_thread().name)
    print('哈哈')
    gevent.sleep(1)
    print('10juqe')
g1 = gevent.spawn(fun1)  # 遇见 认识的IO 会自动切换的模块
g2 = gevent.spawn(fun2)  #

# g1.join()
# g2.join()
gevent.joinall([g1,g2])

#