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
import re
# 返回所有匹配pattern的子串组成的列表, 忽略大小写
print(re.findall('fkit', 'FkIt is very good , Fkit.org is my favorite' , re.I))
# 返回所有匹配pattern的子串组成的迭代器, 忽略大小写
it = re.finditer('fkit', 'FkIt is very good , Fkit.org is my favorite' , re.I)
for e in it:
    print(str(e.start()) + "-->" + e.group())
