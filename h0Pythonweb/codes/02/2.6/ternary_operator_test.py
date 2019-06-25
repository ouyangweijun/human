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
a = 5
b = 3
st = "a大于b" if a > b else  "a不大于b" 
# 输出"a大于b"
print(st)

# 输出"a大于b"
print("a大于b") if a > b else print("a不大于b")

# 第一个返回值部分使用两条语句，逗号隔开
st = print("crazyit"), 'a大于b' if a > b else  "a不大于b" 
print(st)

# 第一个返回值部分使用两条语句，分号隔开
st = print("crazyit"); x = 20 if a > b else  "a不大于b" 
print(st)
print(x)

c = 5
d = 5
# 下面将输出c等于d
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))
