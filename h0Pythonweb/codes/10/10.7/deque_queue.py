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
q = deque(('Kotlin', 'Python'))
# 元素加入队列
q.append('Erlang')
q.append('Swift')
print('q中的元素：' , q)
# 元素出队列，先添加的元素先出队列
print(q.popleft())
print(q.popleft())
print(q)