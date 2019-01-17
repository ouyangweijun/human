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
string = input("请输入一行内容: ")
char_num, digit_num, other_num = 0, 0, 0
for c in string:
    if c.isdigit(): digit_num += 1
    elif c.isalpha(): char_num += 1
    else: other_num += 1
print('字母个数', char_num)
print('数字个数', digit_num)
print('其他字母个数', other_num)
