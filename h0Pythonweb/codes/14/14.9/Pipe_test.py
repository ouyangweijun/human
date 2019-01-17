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

def f(conn):
    print('(%s) 进程开始发送数据...' % multiprocessing.current_process().pid)
    # 使用conn发送数据
    conn.send('Python')
if __name__ == '__main__':
    # 创建Pipe，该函数返回两个PipeConnection对象
    parent_conn, child_conn = multiprocessing.Pipe()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(child_conn, ))
    # 启动子进程
    p.start()
    print('(%s) 进程开始接收数据...' % multiprocessing.current_process().pid)
    # 通过conn读取数据
    print(parent_conn.recv())  # Python
    p.join()