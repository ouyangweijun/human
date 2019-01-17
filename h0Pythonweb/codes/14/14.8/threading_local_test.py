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
from concurrent.futures import ThreadPoolExecutor

# 定义线程局部变量
mydata = threading.local()
# 定义准备作为线程执行体使用的函数
def action (max):
    for i in range(max):
        try:
            mydata.x += i
        except:
            mydata.x = i
        # 访问mydata的x的值
        print('%s mydata.x的值为: %d' % 
            (threading.current_thread().name, mydata.x))
# 使用线程池启动两个子线程
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(action , 10)
    pool.submit(action , 10)
