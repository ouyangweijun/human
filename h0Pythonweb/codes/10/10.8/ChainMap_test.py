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
# 定义3个dict对象
a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}
# 将3个dict对象链在一起，就像变成了一个大的dict
cm = ChainMap(a, b , c)
print(cm)
# 获取Kotlin对应的value
print(cm['Kotlin']) # 90
# 获取Python对应的value
print(cm['Python']) # 86
# 获取Go对应的value
print(cm['Go']) # 93