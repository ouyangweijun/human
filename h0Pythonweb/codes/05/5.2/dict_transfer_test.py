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
def swap(dw):
    # 下面代码实现dw的a、b两个元素的值交换
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("swap函数里，a元素的值是",\
        dw['a'], "；b元素的值是", dw['b'])
    # 把dw直接赋值为None，让它不再指向任何对象
    dw = None
dw = {'a': 6, 'b': 9}
swap(dw)
print("交换结束后，a元素的值是",\
    dw['a'], "；b元素的值是", dw['b'])

