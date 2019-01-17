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
def test(*books ,num) :
    print(books)
    # books被当成元组处理
    for b in books :
        print(b)
    print(num)
# 调用test()函数
test("疯狂iOS讲义", "疯狂Android讲义", num = 20)

my_list = ["疯狂Swift讲义", "疯狂Python讲义"]
# 将列表的多个元素传给支持参数收集的参数
test(my_list, num = 20)
my_tuple= ("疯狂Swift讲义", "疯狂Python讲义")
# 将元组的多个元素传给支持参数收集的参数
test(*my_tuple, num = 20)

