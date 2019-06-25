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
radius = int(input("请输入半径: "))
for i in range(2 * radius + 1):
    half = round((radius ** 2 - (radius - i) ** 2) ** 0.5)
    print("  " * (radius - half), end="")
    print("*", end="")
    print("  " * half * 2, end="")
    print("*")
