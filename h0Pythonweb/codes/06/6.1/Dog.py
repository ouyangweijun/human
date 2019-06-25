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
class Dog:
    # 定义一个jump()方法
    def jump(self):
        print("正在执行jump方法")
    # 定义一个run()方法，run()方法需要借助jump()方法
    def run(self):
        # 使用self参数引用调用run()方法的对象
        self.jump()
        print("正在执行run方法")

d = Dog()
d.run()