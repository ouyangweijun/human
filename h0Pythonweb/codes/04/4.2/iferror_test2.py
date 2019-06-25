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
age = 45
if age > 20 :
    print("青年人")
# 在原本的if条件中增加了else的隐含条件
if age > 40 and not(age > 20) :
    print("中年人")
# 在原本的if条件中增加了else的隐含条件
if age > 60 and not(age > 20) and not(age > 40 and not(age > 20)) :
    print("老年人")