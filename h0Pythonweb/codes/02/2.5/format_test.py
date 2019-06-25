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
price = 108
print("the book's price is %x" % price)
user = "Charli"
age = 8
# 格式化字符串有两个占位符，第三部分提供2个变量
print("%s is a %s years old boy" % (user , age))
num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)
num2 = 30
# 最小宽度为0，左边补0
print("num2 is: %06d" % num2)
# 最小宽度为6，左边补0，总带上符号
print("num2 is: %+06d" % num2)
# 最小宽度为6，右对齐
print("num2 is: %-6d" % num2)
my_value = 3.001415926535
# 最小宽度为8，小数点后保留3位
print("my_value is: %8.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0
print("my_value is: %08.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0，始终带符号
print("my_value is: %+08.3f" % my_value)
the_name = "Charlie"
# 只保留3个字符
print("the name is: %.3s" % the_name) # 输出Cha
# 只保留2个字符，最小宽度10
print("the name is: %10.2s" % the_name)