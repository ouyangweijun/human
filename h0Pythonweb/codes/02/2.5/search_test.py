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
# 判断s是否以crazyit开头
print(s.startswith('crazyit'))
# 判断s是否以site结尾
print(s.endswith('site'))
# 查找s中'org'的出现位置
print(s.find('org')) # 8
# 查找s中'org'的出现位置
print(s.index('org')) # 8
# 从索引为9处开始查找'org'的出现位置
#print(s.find('org', 9)) # -1
# 从索引为9处开始查找'org'的出现位置
print(s.index('org', 9)) # 引发错误
# 将字符串中所有it替换成xxxx
print(s.replace('it', 'xxxx'))
# 将字符串中1个it替换成xxxx
print(s.replace('it', 'xxxx', 1))
# 定义替换表：97（a）->945（α）,98（b）->945（β）,116（t）->964（τ）,
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table)) # crαzyit.org is α good site