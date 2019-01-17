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
while True:
    str_n = input('请输入整数N: ')
    if str_n == 'exit':
        import sys
        sys.exit(0)
    try:
        n = int(str_n)
        if n % 2 != 0:
            print('有趣')
        elif 5 > n > 2:
            print('没意思')
        elif 20 > n > 6:
            print('有趣')
        else:
            print('没意思')
    except:
        print('务必输入整数')
