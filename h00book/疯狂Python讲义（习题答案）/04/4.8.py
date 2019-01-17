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

# 方法一
start = 101
end = 999
for i in range(start, end + 1):
    # 计算百位上的数
    bai = i // 100
    # 计算十位、个位上的数
    shi, ge = (i - bai * 100) // 10, i % 10
    # 判断是否为水仙花数
    if ge ** len(str(i)) + shi ** len(str(i)) + bai ** len(str(i)) == i:
        print(i)

# 方法二
start = 1
end = 10 ** 7
for i in range(start, end + 1):
    sm = 0
    for j in str(i):
        sm += (ord(j) - 48) ** len(str(i))
    # 判断是否为水仙花数
    if sm == i:
        print(i)
    
# 方法三    
a =[j for j in range(1, 10 ** 5) 
    if sum([(ord(i)-48) ** len(str(j)) for i in str(j)]) == j]
print(a)
        
    