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
import threading

# 定义action函数准备作为线程执行体使用
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
  
# 启动子线程
threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被Join的线程")
        jt.start()
        # 主线程调用了jt线程的join()方法，主线程
        # 必须等jt执行结束才会向下执行
        jt.join()
    print(threading.current_thread().name + " " + str(i))

