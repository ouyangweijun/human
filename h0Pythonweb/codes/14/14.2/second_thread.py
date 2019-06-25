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

# 通过继承threading.Thread类来创建线程类
class FkThread(threading.Thread):
    def __init__(self):  
        threading.Thread.__init__(self)
        self.i = 0
    # 重写run()方法作为线程执行体
    def run(self):  
        while self.i < 100:
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() +  " " + str(self.i))
            self.i += 1
# 下面是主程序（也就是主线程的执行体）
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        ft1 = FkThread()
        ft1.start()
        # 创建并启动第二个线程
        ft2 = FkThread()
        ft2.start()
print('主线程执行完成!')