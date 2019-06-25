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
a, b, c = input("请输入第一个字符串:"), input("请输入第二个字符串:"), input("请输入第三个字符串:")
# 创建元组
tuple1 = (a,b,c)
print(tuple1 * 3)
# 创建元组
tuple2 = ("fkjava","crazyit")
# 合并两个元组
print(tuple1 + tuple2)
