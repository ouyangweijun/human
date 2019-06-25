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
name = 'Charlie'
def test ():
    # 声明name是全局变量，后面的赋值语句不会重新定义局部变量
    global name
    # 直接访问name全局变量
    print(name)  # Charlie
    name = '孙悟空'
test()
print(name)  # 孙悟空
