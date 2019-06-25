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
f = codecs.open("for_file.py", 'r', 'utf-8', buffering=True)
# 使用for循环遍历文件对象
for line in f:
    print(line, end='')
f.close()
# 将文件对象转换为list列表
print(list(codecs.open("for_file.py", 'r', 'utf-8', buffering=True)))
