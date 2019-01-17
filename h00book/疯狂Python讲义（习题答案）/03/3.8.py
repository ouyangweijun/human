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
import random

char_list = input("请输入空格隔开的大写字母:").split()
char_dict = {}.fromkeys(char_list)
print(char_dict)
for k in char_dict.keys():
    char_dict[k] = char_list.count(k)
print(char_dict)
