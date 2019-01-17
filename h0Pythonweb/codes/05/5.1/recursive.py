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
def fn(n) :
	if n == 0 :
		return 1
	elif n == 1 :
		return 4
	else :
		# 函数中调用它自身，就是函数递归
		return 2 * fn(n - 1) + fn(n - 2)
# 输出fn(10)的结果
print("fn(10)的结果是:", fn(10))
