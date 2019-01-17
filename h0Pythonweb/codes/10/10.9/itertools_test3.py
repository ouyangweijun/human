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
import itertools as it
# 使用两个序列进行排列组合
for e in it.product('AB', 'CD'):
    print(''.join(e), end=', ') # AC, AD, BC, BD,
print('\n---------')
# 使用一个序列、重复2次进行全排列
for e in it.product('AB', repeat=2):
    print(''.join(e), end=', ') # AA, AB, BA, BB,
print('\n---------')
# 从序列中取2个元素进行排列
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=', ') # AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC,
print('\n---------')
# 从序列中取2个元素进行组合、元素不允许重复
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=', ') # AB, AC, AD, BC, BD, CD,
print('\n---------')
# 从序列中取2个元素进行组合、元素允许重复
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=', ') # AA, AB, AC, AD, BB, BC, BD, CC, CD, DD,
