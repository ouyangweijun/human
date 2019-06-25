#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-24 06:47
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 1.协程的切换.py
# @Desc     :


import time

from greenlet import greenlet  # 在单线程中，切换状态的代码的模块
def eat1():
    print('吃鸡1')
    g2.switch()
    time.sleep(5)
    print('吃鸡翅2')
    g2.switch()

def eat2():
    print('吃饺子')
    g1.switch()
    time.sleep(3)
    print('吃白切鸡')

g1 = greenlet(eat1)
g2 = greenlet(eat2)

g1.switch()


# 切换 不能规避IO 时间
#