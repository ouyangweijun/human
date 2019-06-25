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
    string = input('请输入手机号: ')
    if string == 'exit':
        sys.exit(0)
    if re.fullmatch('^(1[358][0-9]|14[579]|16[6]|17[0135678]|19[89])\d{8}$', string):
        print('是手机号码')
    else:
        print('不是手机号码')
    