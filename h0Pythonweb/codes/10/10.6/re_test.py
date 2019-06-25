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
# 编译得到正则表达式对象
pa = re.compile('fkit')
# 调用match方法，原本应该从开始匹配，
# 此处指定从索引为4的地方开始匹配，就可以成功匹配了
print(pa.match('www.fkit.org', 4).span()) # (4, 8)
# 此处指定从索引为4到索引6之间执行匹配，匹配失败
print(pa.match('www.fkit.org', 4, 6)) # None
# 此处指定从索引为4到索引8之间执行全匹配，匹配成功
print(pa.fullmatch('www.fkit.org', 4, 8).span()) # (4, 8)