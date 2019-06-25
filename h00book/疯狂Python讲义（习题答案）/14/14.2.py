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
import threading, queue, time

bq = queue.Queue(1)
lock = threading.RLock()
def action1(bq):
    for i in range(1, 53, 2):
        bq.put(i)
        print(i, end='')
        print(i + 1, end='')
def action2(bq):
    for i in range(26):
        bq.get()
        print(chr(65 + i), end='')

# 创建并启动第一个线程
t1 =threading.Thread(target=action1, args=(bq, ))
t1.start()
# 创建并启动第二个线程
t2 =threading.Thread(target=action2, args=(bq, ))
t2.start()
