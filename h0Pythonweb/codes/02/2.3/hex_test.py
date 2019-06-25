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
# 以0x或0X开头的整数数值是十六进制的整数
hex_value1 = 0x13
hex_value2 = 0XaF
print("hexValue1的值为：", hex_value1)
print("hexValue2的值为：", hex_value2)
# 以0b或0B开头的整数数值是二进制的整数
bin_val = 0b111
print('bin_val的值为：', bin_val)
bin_val = 0B101
print('bin_val的值为：', bin_val)
# 以0o或0O开头的整数数值是二进制的整数
oct_val = 0o54
print('oct_val的值为：', oct_val)
oct_val = 0O17
print('oct_val的值为：', oct_val)
# 在数值中使用下画线
one_million = 1_000_000
print(one_million)
price = 234_234_234 # price实际的值为234234234
android = 1234_1234 # android实际的值为12341234
