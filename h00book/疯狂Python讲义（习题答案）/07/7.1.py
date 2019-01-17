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
str_n = input('请输入整数N: ')
try:
    n = int(str_n)
    print(n)
    i = 0
    while True:
        try:
            a , b = input('请输入2个整数(空格隔开): ').split()
            print(int(a) // int(b))
            i += 1
            if i >= n: break
        except:
            print('务必输入空格隔开的2个整数!')
except:
    print('请输入整数N!')
