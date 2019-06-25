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
i = 100
f = 88.99
print(i)
print(type(i))
print(f)
print(type(f))

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

af1 = 5.2345556
# 输出af1的值
print("af1的值为:", af1)
af2 = 25.2345
print("af2的类型为:", type(af2))
f1 = 5.12e2
print("f1的值为:", f1)
f2 = 5e3
print("f2的值为:", f2)
print("f2的类型为:", type(f2)) # 看到类型为float

ac1 = 3 + 0.2j
print(ac1)
print(type(ac1)) # 输出 complex类型
ac2 = 4 - 0.1j
print(ac2)
# 复数运行
print(ac1 + ac2) # 输出 (7+0.1j)
