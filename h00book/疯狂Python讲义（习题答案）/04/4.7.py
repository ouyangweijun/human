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
start = 101
end = 200
for i in range(101, end + 1):
    is_prime = True
    for j in range(2 , int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
        
    