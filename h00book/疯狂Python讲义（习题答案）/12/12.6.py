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
    dir_count = file_count = 0
    for x in p.iterdir():
        if Path(x).is_dir():
            dir_count += 1
        else:
            file_count += 1
    return dir_count, file_count
dir_str = input('请输入路径: ')
p = Path(dir_str)
if not p.exists() or not p.is_dir():
    raise ValueError('您输入的不是有效的路径')
dir_count, file_count = process_dir(p)
print('%s 目录下有%d个文件' % (dir_str, file_count))
print('%s 目录下有%d个目录' % (dir_str, dir_count))
