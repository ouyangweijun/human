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
import random

def fn(n):
    # 输出矩阵
    for i in range(n):
        for j in range(n):
            print(' %2d ' % (i * n + j + 1), end="")
        print()
    print('-' * (4 * n))
    # 输出转置矩阵
    for i in range(n):
        for j in range(n):
            print(' %2d ' % (j * n + i + 1), end="")
        print()

n = int(input("请输入整数n:"))
fn(n)