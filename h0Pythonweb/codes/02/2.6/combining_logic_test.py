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
#bookName = "疯狂Python"
#price = 79
#version = "正式版"
#if bookName.endswith('Python') and price < 50 or version == "正式版" :
#    print("打算购买这本Python图书")
#else:
#	print("不购买！")

bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith('Python') and (price < 50 or version == "正式版") :
    print("打算购买这本Python图书")
else:
	print("不购买！")
