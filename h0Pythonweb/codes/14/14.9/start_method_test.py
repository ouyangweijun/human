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
import multiprocessing
import os

def foo(q):
    print('被启动的新进程: (%s)' % os.getpid())
    q.put('Python')
if __name__ == '__main__':
    # 设置使用fork方式启动进程
    multiprocessing.set_start_method('spawn')
    q = multiprocessing.Queue()
    # 创建进程
    mp = multiprocessing.Process(target=foo, args=(q, ))
    # 启动进程
    mp.start()
    # 获取队列中的消息 
    print(q.get())
    mp.join()
