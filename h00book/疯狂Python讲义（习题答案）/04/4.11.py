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
lines = int(input("请输入一半的行数: "))
# 打印上半
for i in range(lines):
    print("-" * (lines * 2 - 2 - 2 * i), end="")
    my_list = []
    for j in range(i + 1):
        my_list.append(chr(96 + lines - j))
    for j in range(i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (lines * 2 - 2 - 2 * i))
# 打印下半
for i in range(lines - 1):
    print("-" * (2 * (i + 1)), end="")
    # 换一种方式初始化list列表
    my_list = [chr(96 + lines - j) for j in range(lines - 1 - i)]
    for j in range(lines - 2 - i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (2 * (i + 1)))

