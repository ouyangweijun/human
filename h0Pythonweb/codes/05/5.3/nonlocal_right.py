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
def foo ():
    # 局部变量name
    name = 'Charlie'
    def bar ():
        nonlocal name
        # 访问bar函数所在的foo函数的name局部变量
        print(name) # Charlie
        name = '孙悟空'
    bar()
foo()