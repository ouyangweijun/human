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
size = int(input("输入要打印的SIZE(奇数):"))
array = [[0] * size]
# 创建一个长度size * size的二维列表
for i in range(size - 1):
    array += [[0] * size]
row, col = 0, size // 2
for i in range(1, size * size + 1):
    array[row][col] = i
    if i % size == 0:
        row += 1
    elif row == 0:
        row = size - 1
        col += 1
    elif col == size - 1:
        row -= 1
        col = 0
    else:
        row -= 1
        col += 1
for i in range(size):
    for j in range(size):
        print('%02d' % array[i][j], end=" ")
    print()
    
    