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
import sys
import re

# 定义匹配Email的正则表达式
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
    + '[\.][a-z]{2,3}([\.][a-z]{2})?'
# 读取标准输入
text = sys.stdin.read()
# 使用正则表达式执行查找
it = re.finditer(mailPattern, text , re.I)
# 输出所有的电子邮件
for e in it:
    print(str(e.span()) + "-->" + e.group())
