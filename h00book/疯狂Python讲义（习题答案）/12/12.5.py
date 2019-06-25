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

def process_dir(p):
    for x in p.iterdir():
        if Path(x).is_dir():
            process_dir(Path(x))
        else:
            print(x)
dir_str = input('请输入路径: ')
p = Path(dir_str)
if not p.exists() or not p.is_dir():
    raise ValueError('您输入的不是有效的路径')
process_dir(p)