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

# 比较两个Unix风格的路径，区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO')) # False
# 比较两个Windows风格的路径，不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO')) # True
# Windows风格的路径不区分大小写
print(PureWindowsPath('INFO') in { PureWindowsPath('info') })#True
# Unix风格的路径区分大小写,所以'D:'小于'c:'
print(PurePosixPath('D:') < PurePosixPath('c:')) # True
# Windows风格的路径不区分大小写,所以'd:'（D:）大于'c:'
print(PureWindowsPath('D:') > PureWindowsPath('c:')) #True


# 不同风格的路径可以判断是否相等（总不相等）
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit')) # False
# 不同风格的路径不能判断大小，否则会引发异常
#print(PureWindowsPath('info') < PurePosixPath('info')) # TypeError

pp = PureWindowsPath('abc')
# 将多个路径拼起来（Windows风格的路径）
print(pp / 'xyz' / 'wawa') # abc\xyz\wawa
pp = PurePosixPath('abc')
# 将多个路径拼起来（Unix风格的路径）
print(pp / 'xyz' / 'wawa') # abc/xyz/wawa
pp2 = PurePosixPath('haha', 'hehe')
# 将pp、pp2两个路径连接起来
print(pp / pp2) # abc/haha/hehe

pp = PureWindowsPath('abc', 'xyz', 'wawa')
print(str(pp)) # abc\xyz\wawa
pp = PurePosixPath('abc', 'xyz', 'wawa')
print(str(pp)) # abc/xyz/wawa