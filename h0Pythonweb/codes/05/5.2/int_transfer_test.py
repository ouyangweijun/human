# coding: utf-8
#########################################################################
# 网站: <a href="http:#www.crazyit.org">疯狂Java联盟</a>               #
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
def swap(a , b) :
    # 下面代码实现a、b变量的值交换
    a, b = b, a
    print("swap函数里，a的值是", \
        a, "；b的值是", b)
a = 6
b = 9
swap(a , b)
print("交换结束后，变量a的值是", \
    a , "；变量b的值是", b)
