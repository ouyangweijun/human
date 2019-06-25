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
with open('text1.txt') as f1:
    text1 = f1.read()
with open('text2.txt') as f2:
    text2 = f2.read()
rvt = (list(text1) + list(text2))
rvt.sort()
with open('text3.txt', 'w+') as f3:
    f3.write("".join(rvt))
