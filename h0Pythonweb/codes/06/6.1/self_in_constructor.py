# coding: utf-8
#########################################################################
# 网站: <a href="http:#www.crazyit.org">疯狂Java联盟</a>               #
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
class InConstructor :
    def __init__(self) :
        # 在构造方法里定义一个foo变量（局部变量）
        foo = 0
        # 使用self代表该构造方法正在初始化的对象
        # 下面的代码将会把该构造方法正在初始化的对象的foo实例变量设为6
        self.foo = 6
# 所有使用InConstructor创建的对象的foo实例变量将被设为6
print(InConstructor().foo) # 输出6
