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
# 定义了支持参数收集的函数
def test(x, y, z=3, *books, **scores) :
    print(x, y, z)
    print(books)
    print(scores)
test(1, 2, 3, "疯狂iOS讲义" , "疯狂Android讲义", 语文=89, 数学=94)
test(1, 2, "疯狂iOS讲义" , "疯狂Android讲义", 语文=89, 数学=94)
test(1, 2, 语文=89, 数学=94)



