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
# 定义一个打印三角形的函数，有默认值的参数必须放在后面
def printTriangle(char, height = 5) :
	for i in range(1, height + 1) :
		# 先打印一排空格
		for j in range(height - i) :
			print(' ', end = '')
		# 再打印一排特殊字符
		for j in range(2 * i - 1) :
			print(char, end = '')
		print()
printTriangle('@', 6)
printTriangle('#', height=7)
printTriangle(char = '*')
