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
def my_max(x, y) : 
    '''
    获取两个数值之间较大数的函数。

    my_max(x, y)
        返回x、y两个参数之间较大的那个
    '''
    # 定义一个变量z，该变量等于x、y中较大的值
    z = x if x > y else y
    # 返回变量z的值
    return z
# 使用help()函数查看my_max的帮助文档
help(my_max)
print(my_max.__doc__)