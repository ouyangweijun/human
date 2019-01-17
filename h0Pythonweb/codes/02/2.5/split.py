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
s = 'crazyit.org is a good site'
# 使用空白对字符串进行分割
print(s.split()) # 输出 ['crazyit.org', 'is', 'a', 'good', 'site']
# 使用空白对字符串进行分割,最多只分割前2个单词
print(s.split(None, 2)) # 输出 ['crazyit.org', 'is', 'a good site']
# 使用点进行分割
print(s.split('.')) # 输出 ['crazyit', 'org is a good site']
mylist = s.split()
# 使用'/'为分割符，将mylist连接成字符串
print('/'.join(mylist)) # 输出 crazyit.org/is/a/good/site
# 使用','为分割符，将mylist连接成字符串
print(','.join(mylist)) # 输出 crazyit.org,is,a,good,site