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

# 访问drive属性
print(PureWindowsPath('c:/Program Files/').drive) # c:
print(PureWindowsPath('/Program Files/').drive) # ''
print(PurePosixPath('/etc').drive) # ''

# 访问root属性
print(PureWindowsPath('c:/Program Files/').root) # \
print(PureWindowsPath('c:Program Files/').root) # ''
print(PurePosixPath('/etc').root) # /

# 访问anchor属性
print(PureWindowsPath('c:/Program Files/').anchor) # c:\
print(PureWindowsPath('c:Program Files/').anchor) # c:
print(PurePosixPath('/etc').anchor) # /

# 访问parents属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0]) # abc\xyz\wawa
print(pp.parents[1]) # abc\xyz
print(pp.parents[2]) # abc
print(pp.parents[3]) # .
# 访问parent属性
print(pp.parent) # abc\xyz\wawa

# 访问name属性
print(pp.name) # haha
pp = PurePath('abc/wawa/bb.txt')
print(pp.name) # bb.txt

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问suffixes属性
print(pp.suffixes[0]) # .txt
print(pp.suffixes[1]) # .tar
print(pp.suffixes[2]) # .zip
# 访问suffix属性
print(pp.suffix) # .zip
print(pp.stem) # bb.txt.tar

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp) # abc\xyz\wawa\haha
# 转成Unix风格的路径
print(pp.as_posix()) # abc/xyz/wawa/haha
# 将相对路径转换成Uri引发异常
#print(pp.as_uri()) # ValueError
# 创建绝对路径
pp = PurePath('d:/', 'Python', 'Python3.6')
# 将绝对路径转换成Uri
print(pp.as_uri()) # file:///d:/Python/Python3.6

# 判断当前路径是否匹配指定模式
print(PurePath('a/b.py').match('*.py')) # True
print(PurePath('/a/b/c.py').match('b/*.py')) # True
print(PurePath('/a/b/c.py').match('a/*.py')) # False

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试relative_to方法
print(pp.relative_to('c:/'))  # abc\xyz\wawa
print(pp.relative_to('c:/abc'))  # xyz\wawa
print(pp.relative_to('c:/abc/xyz'))  # wawa

# 测试with_name方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py')) # e:\Downloads\fkit.py
p = PureWindowsPath('c:/')
#print(p.with_name('fkit.py')) # ValueError

# 测试with_suffix方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))  # e:\Downloads\pathlib.tar.zip
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))  # README.txt
