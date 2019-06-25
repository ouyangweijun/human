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
q = deque(range(5))
print('q中的元素：' , q)
# 执行旋转，使之首尾相连
q.rotate()
print('q中的元素：' , q)
# 再次执行旋转，使之首尾相连
q.rotate()
print('q中的元素：' , q)