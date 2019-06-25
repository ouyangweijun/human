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
def fibonacci(n):
    rvt_list = [1, 1]
    # 生成fibonacci数列
    [rvt_list.append(rvt_list[-1] + rvt_list[-2]) for i in range(2, n)]
    return rvt_list
print(fibonacci(10))
# 计算fibonacci数列的元素的平方
x = map(lambda x: x*x , fibonacci(10))
print([e for e in x])