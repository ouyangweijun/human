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
import re
string, sub = input("请输入第一个字符串: "), input('请输入子串: ')
matches = list(re.finditer(r'(?={})'.format(sub), string))
if matches:
    print('\n'.join(str((match.start(),
        match.start() + len(sub) - 1)) for match in matches))
else:
    print('(-1, -1)')