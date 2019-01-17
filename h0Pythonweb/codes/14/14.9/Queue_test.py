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

def f(q):
    print('(%s) 进程开始放入数据...' % multiprocessing.current_process().pid)
    q.put('Python')
if __name__ == '__main__':
    # 创建进程通信的Queue
    q = multiprocessing.Queue()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(q,))
    # 启动子进程
    p.start()
    print('(%s) 进程开始取出数据...' % multiprocessing.current_process().pid)
    # 取出数据
    print(q.get())  # Python
    p.join()