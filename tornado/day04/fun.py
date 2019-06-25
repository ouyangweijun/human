#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-23 23:28
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : fun.py
# @Desc     :

#1.协程

#func

# func

# 协程 ，在一个线程 一个之间切换

# 1.协程
# 2.如何实现两个函数之间的切换

# def func1():
#     print('1')
#     yield
#     print(3)
#     yield
# def func2():
#     g = func1()
#     next(g)
#     print(2)
#     next(g)
#     print(4)
#
# func2()


# def consumer():
#     while True:
#         n = yield
#         print('消费啦一个包子%s' % n)
# def producer():
#     g = consumer()
#     next(g)
#     for i in range(10):
#         print('生产包子 %s ' % i)
#         g.send(i)
# producer()



from greenlet import greenlet  # 在单线程中，切换状态的代码的模块
def eat1():
    print('吃鸡1')
    g2.switch()
    print('吃鸡翅2')
    g2.switch()

def eat2():
    print('吃饺子')
    g1.switch()


g1 = greenlet(eat1)
g2 = greenlet(eat2)

g1.switch()