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
import time
import os

# 定义一个准备作为进程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print('(%s)进程正在执行: %d' % (os.getpid(), i))
        my_sum += i
    return my_sum
if __name__ == '__main__':
    # 创建一个包含4条进程的进程池
    with multiprocessing.Pool(processes=4) as pool:
        # 使用进程执行map计算
        # 后面元组有3个元素，因此程序启动3条进程来执行action函数
        results = pool.map(action, (50, 100, 150))
        print('--------------')
        for r in results:
            print(r)

    