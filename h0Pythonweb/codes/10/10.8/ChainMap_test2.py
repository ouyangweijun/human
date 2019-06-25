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
from collections import ChainMap
import builtins
my_name = '孙悟空'
def test():
    my_name = 'yeeku'
    # 将locals、globals、buliltins的变量链接成ChainMap
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    # 访问my_name对应的value，优先使用局部范围的定义
    print(pylookup['my_name']) # 'yeeku'
    # 访问len对应的value，由于局部范围、全区范围都找不到，因此访问内置定义的len函数
    print(pylookup['len']) # <built-in function len>
test()