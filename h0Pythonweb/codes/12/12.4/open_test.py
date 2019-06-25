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
# 以默认方式打开文件
f = open('open_test.py')
# 访问文件的编码方式
print(f.encoding) # cp936
# 访问文件的访问模式
print(f.mode) # r
# 访问文件是否已经关闭
print(f.closed) # False
# 访问文件对象打开的文件名
print(f.name) # open_test.py