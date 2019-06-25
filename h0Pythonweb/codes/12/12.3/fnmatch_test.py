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
import fnmatch

# 遍历当前目录下所有文件和子目录
for file in Path('.').iterdir():
    # 访问所有以_test.py结尾的文件
    if fnmatch.fnmatch(file, '*_test.PY'):
        print(file)

names = ['a.py', 'b.py', 'c.py', 'd.py']
# 对names列表进行过滤
sub = fnmatch.filter(names, '[ac].py')
print(sub) # ['a.py', 'c.py']

print(fnmatch.translate('?.py')) # (?s:.\.py)\Z
print(fnmatch.translate('[ac].py')) # (?s:[ac]\.py)\Z
print(fnmatch.translate('[a-c].py')) # (?s:[a-c]\.py)\Z