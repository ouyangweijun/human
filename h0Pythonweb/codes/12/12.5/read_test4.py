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
f = codecs.open("read_test4.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读到数据，跳出循环
    if not ch: break
    # 输出ch
    print(ch, end='')
f.close()