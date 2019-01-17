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
import sys
# 定义一个字符串列表
my_list = ["Hello" , "Python" , "Spring"]
# 使用异常处理来遍历arr数组的每个元素
try:
    i = 0
    while True:
       print(my_list [i])
       i += 1
except:
    pass

i = 0
while i < len(my_list):
   print(my_list [i])
   i += 1