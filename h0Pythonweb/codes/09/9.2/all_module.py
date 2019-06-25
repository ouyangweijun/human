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
'测试__all__变量的模块'

def hello():
    print("Hello, Python")
def world():
    print("Pyhton World is funny")
def test():
    print('--test--')

# 定义__all__变量，指定默认只导入hello和world两个程序单元
__all__ = ['hello', 'world']