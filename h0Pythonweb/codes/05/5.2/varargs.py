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
def test(a, *books) :
    print(books)
    # books被当成元组处理
    for b in books :
        print(b)
    # 输出整数变量a的值
    print(a)
# 调用test()函数
test(5 , "疯狂iOS讲义" , "疯狂Android讲义")
