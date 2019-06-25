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
# 传入计算平方的lambda表达式作为参数
x = map(lambda x: x*x , range(8))
print([e for e in x]) # [0, 1, 4, 9, 16, 25, 36, 49]
# 传入计算平方的lambda表达式作为参数
y = map(lambda x: x*x if x % 2 == 0 else 0, range(8))
print([e for e in y]) # [0, 0, 4, 0, 16, 0, 36, 0]

