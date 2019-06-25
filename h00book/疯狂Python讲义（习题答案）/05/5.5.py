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
def fn(n):
    if n < 2:
        exit()
    sum = 1
    for i in range(2, n+1):
        sum += i ** 3
    return sum
n = int(input("请输入数字:"))
result = fn(n)
print("1～%d的立方和是%d" % (n, result))