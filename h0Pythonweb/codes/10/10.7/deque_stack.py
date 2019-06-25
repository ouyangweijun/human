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
from collections import deque
stack = deque(('Kotlin', 'Python'))
# 元素入栈
stack.append('Erlang')
stack.append('Swift')
print('stack中的元素：' , stack)
# 元素出栈，后添加的元素先出栈
print(stack.pop())
print(stack.pop())
print(stack)