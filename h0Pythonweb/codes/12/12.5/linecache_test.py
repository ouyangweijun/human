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
import linecache
import random

# 读取random模块的源文件的第3行
print(linecache.getline(random.__file__, 3))
# 读取本程序的第3行
print(linecache.getline('linecache_test.py', 3))
# 读取普通文件的第2行
print(linecache.getline('utf_text.txt', 2))
