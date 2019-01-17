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
from pathlib import *

# 获取当前目录
p = Path('.')
# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上一级目录
p = Path('../')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/*.py'):
    print(x)

# 获取g:/publish/codes对应的目录
p = Path('g:/publish/codes')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/Path_test1.py'):
    print(x)
