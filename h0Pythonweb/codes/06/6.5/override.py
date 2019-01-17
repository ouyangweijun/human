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
class Bird: 
    # Bird类的fly()方法
    def fly(self):
        print("我在天空里自由自在地飞翔...")
class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("我只能在地上奔跑...")
  
# 创建Ostrich对象
os = Ostrich()
# 执行Ostrich对象的fly()方法，将输出"我只能在地上奔跑..."
os.fly()

   