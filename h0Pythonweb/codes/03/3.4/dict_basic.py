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
scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])
# 对不存在的key赋值，就是增加key-value对
scores['数学'] = 93
scores[92] = 5.7
print(scores) # {'语文': 89, '数学': 93, 92: 5.7}
# 使用del语句删除key-value对
del scores['语文']
del scores['数学']
print(scores) # {92: 5.7}

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 对存在的key-value对赋值，改变key-value对
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars) # {'BMW': 8.5, 'BENS': 4.3, 'AUDI': 3.8}

# 判断cars是否包含名为'AUDI'的key
print('AUDI' in cars) # True
# 判断cars是否包含名为'PORSCHE'的key
print('PORSCHE' in cars) # False
print('LAMBORGHINI' not in cars) # True
