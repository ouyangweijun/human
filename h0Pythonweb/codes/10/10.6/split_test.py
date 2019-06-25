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
# 使用逗号对字符串进行分割
print(re.split(', ', 'fkit, fkjava, crazyit'))
# 输出：['fkit', 'fkjava', 'crazyit']
# 指定只分割1次，被切分成2个子串
print(re.split(', ', 'fkit, fkjava, crazyit', 1))
# 输出：['fkit', 'fkjava, crazyit']
# 使用a进行分割
print(re.split('a', 'fkit, fkjava, crazyit'))
# 输出：['fkit, fkj', 'va, crazyit']
# 使用x进行分割，没有匹配内容，则不会执行分割
print(re.split('x', 'fkit, fkjava, crazyit'))
# 输出：['fkit, fkjava, crazyit']


#print(re.split('\W+', ' runoob, runoob, runoob.'))
#['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
#re.split('\W+', ' runoob, runoob, runoob.', 1) 
#['', 'runoob, runoob, runoob.']
# 
#>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
#['hello world']