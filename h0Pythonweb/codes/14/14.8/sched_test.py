# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import sched, time
import threading

# 定义线程调度器
s = sched.scheduler()

# 定义被调度的函数
def print_time(name='default'):
    print("%s 的时间: %s" % (name, time.ctime()))
print('主线程：', time.ctime())
# 指定10秒之后执行print_time函数
s.enter(10, 1, print_time)
# 指定5秒之后执行print_time函数，优先级为2
s.enter(5, 2, print_time, argument=('位置参数',))
# 指定5秒之后执行print_time函数，优先级为1
s.enter(5, 1, print_time, kwargs={'name': '关键字参数'})
# 执行调度的任务
s.run()
print('主线程：', time.ctime())
