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
import re, sys

while True:
    string = input('输入字符串: ')
    if string == 'exit':
        sys.exit(0)
    if not re.fullmatch('[0-9,\.]+', string):
        raise ValueError("您的输入只能包含0-9数字、英文逗号、英文点号")
    rt_list = re.findall('[0-9]+', string)
    print(rt_list)