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
    for  i in range(100):
        print(threading.current_thread().name +  " " + str(i))
# 创建线程对象
sd = threading.Thread(target=action, args=(100,))
for i in range(300):
    # 调用threading.current_thread()函数获取当前线程
    print(threading.current_thread().name +  " " + str(i))
    if i == 20:
        # 启动线程
        sd.start()
        # 判断启动后线程的is_alive()值，输出True
        print(sd.is_alive())
    # 当线程处于新建、死亡两种状态时，is_alive()方法返回False
    # 当i > 20时，该线程肯定已经启动过了，如果sd.is_alive()为False时
    # 那就是死亡状态了
    if i > 20 and not(sd.is_alive()):
        # 试图再次启动该线程
        sd.start()
