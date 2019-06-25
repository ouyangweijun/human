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
# 循环的初始化条件
count_i = 0
# 当count_i小于10时，执行循环体
while count_i < 10 :
    print("count:", count_i)
    # 迭代语句
    count_i += 1
print("循环结束!")

# 下面是一个死循环
count_i2 = 0
while count_i2 < 10 :
    print("不停执行的死循环:", count_i2)
    count_i2 -=1
print("永远无法跳出的循环体")

