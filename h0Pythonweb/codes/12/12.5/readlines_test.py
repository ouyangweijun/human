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
import codecs
# 指定使用utf-8字符集读取文件内容
f = codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True)
# 使用readlines()读取所有行，返回所有行组成的列表
for l in f.readlines():
    print(l, end='')
f.close()