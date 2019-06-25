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
# 定义一个函数
def girth(width , height): 
	print("width: ", width)
	print("height: ", height)
	return 2 * (width + height)
# 传统调用函数的方式，根据位置传入参数
print(girth(3.5, 4.8))
# 根据关键字参数来传入参数
print(girth(width = 3.5, height = 4.8))
# 使用关键字参数时可交换位置
print(girth(height = 4.8, width = 3.5))
# 部分使用关键字参数，部分使用位置参数
print(girth(3.5, height = 4.8))

# 位置参数必须放在关键字参数之前，下面代码错误
print(girth(width = 3.5, 4.8))

