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
f = open('filept_test.py', 'rb')
# 判断文件指针的位置
print(f.tell()) # 0
# 将文件指针移动到3处
f.seek(3)
print(f.tell()) # 3
# 读取一个字节，文件指针自动后移1个数据
print(f.read(1)) # o
print(f.tell())  # 4
# 将文件指针移动到5处
f.seek(5)
print(f.tell())  # 5
# 将文件指针向后移动5个数据
f.seek(5, 1)
print(f.tell())  # 10
# 将文件指针移动到倒数第10处
f.seek(-10, 2)
print(f.tell())
print(f.read(1))  # d