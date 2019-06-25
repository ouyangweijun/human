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
f = codecs.open("readline_test.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一行
    line = f.readline()
    # 如果没有读到数据，跳出循环
    if not line: break
    # 输出line
    print(line, end='')
f.close()