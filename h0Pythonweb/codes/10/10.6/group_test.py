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
# 在正则表达式中使用组
m = re.search(r'(fkit).(org)', r"www.fkit.org is a good domain")
print(m.group(0)) # fkit.org
# 调用简化写法，底层是调用m.__getitem__(0)
print(m[0]) # fkit.org
print(m.span(0)) # (4, 12)
print(m.group(1)) # fkit
# 调用简化写法，底层是调用m.__getitem__(1)
print(m[1]) # fkit
print(m.span(1)) # (4, 8)
print(m.group(2)) # org
# 调用简化写法，底层是调用m.__getitem__(2)
print(m[2]) # org
print(m.span(2)) # (9, 12)
# 返回所有组所匹配的字符串组成的元组
print(m.groups())

# 正则表达式定义了2个组，并为组指定了名字
m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)',\
    r"www.fkit.org is a good domain")
print(m2.groupdict()) # {'prefix': 'fkit', 'suffix': 'org'}