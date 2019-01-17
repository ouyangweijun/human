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

# 创建PurePath，实际上使用PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))  # <class 'pathlib.PureWindowsPath'>
pp = PurePath('crazyit', 'some/path', 'info')
# 看到输出Windows风格的路径
print(pp) # 'crazyit\some\path\info'
pp = PurePath(Path('crazyit'), Path('info'))
# 看到输出Windows风格的路径
print(pp) # 'crazyit\info'
# 明确指定创建PurePosixPath
pp = PurePosixPath('crazyit', 'some/path', 'info')
# 看到输出Unix风格的路径
print(pp) # crazyit/some/path/info


# 如果不传入参数，默认使用当前路径
pp = PurePath()
print(pp) # .


# 如果传入参数包含多个根路径，则只有最后一个根路径及后面子路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp) # /usr/lib64
pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp) # d:info

# 在Windows风格路径中，只有盘符才算根路径
pp = PureWindowsPath('c:/Windows', '/Program Files')
print(pp) # c:\Program Files

# 路径字符串中多出来的斜杠和点号（代表当前路径）都会被忽略
pp = PurePath('crazyit//info')
print(pp) # crazyit\info
pp = PurePath('crazyit/./info')
print(pp) # crazyit\info
pp = PurePath('crazyit/../info')
print(pp) # crazyit\..\info，相当于找和crazyit同一级的info路径