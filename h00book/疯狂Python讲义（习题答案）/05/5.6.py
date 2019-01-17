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
    result_list = [1]
    for i in range(n):
        result_list.append(result_list[-1] * len(result_list))
    return result_list[-1]

n = int(input("请输入数字:"))
result = fn(n)
print("%d的阶乘是%d" % (n, result))