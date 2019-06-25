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
## 定义一个函数，声明2个形参
#def my_max(x, y) : 
#	# 定义一个变量z，该变量等于x、y中较大的值
#	z = x if x > y else y
#	# 返回变量z的值
#	return z
def my_max(x, y) : 
	# 返回一个表达式
	return x if x > y else y

# 定义一个函数，声明一个形参
def say_hi(name) :
	print("===正在执行say_hi()函数===")
	return name + "，您好！"
a = 6
b = 9
# 调用my_max()函数，将函数返回值赋值给result变量
result = my_max(a , b) # ①
print("result:", result)
# 调用say_hi()函数，直接输出函数的返回值
print(say_hi("孙悟空")) # ②
