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
# 字符串模板中使用key
temp = '书名是:%(name)s, 价格是:%(price)010.2f, 出版社是:%(publish)s'
book = {'name':'疯狂Python讲义', 'price': 88.9, 'publish': '电子社'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'疯狂Kotlin讲义', 'price': 78.9, 'publish': '电子社'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
