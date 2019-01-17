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
stack = []
# 向栈中“入栈”3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack) # ['fkit', 'crazyit', 'Charlie']
# 第一次出栈：最后入栈的元素被移出栈
print(stack.pop())
print(stack) # ['fkit', 'crazyit']
# 再次出栈
print(stack.pop())
print(stack) # ['fkit']
