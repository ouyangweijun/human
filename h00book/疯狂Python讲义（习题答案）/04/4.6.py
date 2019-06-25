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
while(True):
    s = input("输入自己的成绩:")
    if s == 'exit':
        import sys
        sys.exit(0)
    score = float(s)
    if score >= 90:
        print('A')
    elif 90 > score >= 80:
        print('B')
    elif 80 > score >= 70:
        print('C')
    else:
        print('D')
