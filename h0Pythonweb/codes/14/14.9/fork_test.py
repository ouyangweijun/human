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
import os

print('父进程（%s）开始执行' % os.getpid())
# 开始fork一个子进程
# 从这行代码开始，下面代码都会被两个进程执行
pid = os.fork()
print('进程进入：%s' % os.getpid())
# 如果pid为0，表明子进程
if pid == 0:
    print('子进程，其ID为 (%s)， 父进程ID为 (%s)' % (os.getpid(), os.getppid()))
else:
    print('我 (%s) 创建的子进程ID为 (%s).' % (os.getpid(), pid))
print('进程结束：%s' % os.getpid())
