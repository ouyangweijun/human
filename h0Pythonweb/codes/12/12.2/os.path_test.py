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
import os
import time

# 获取绝对路径
print(os.path.abspath("abc.txt")) # G:\publish\codes\12\12.2\abc.txt
# 获取共同前缀
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib'])) # /usr/l
# 获取共同路径
print(os.path.commonpath(['/usr/lib', '/usr/local/lib'])) # \usr
# 获取目录
print(os.path.dirname('abc/xyz/README.txt')) #abc/xyz
# 判断指定目录是否存在 
print(os.path.exists('abc/xyz/README.txt')) # False
# 获取最近一次访问时间
print(time.ctime(os.path.getatime('os.path_test.py')))
# 获取最后一次修改时间
print(time.ctime(os.path.getmtime('os.path_test.py')))
# 获取创建时间
print(time.ctime(os.path.getctime('os.path_test.py')))
# 获取文件大小
print(os.path.getsize('os.path_test.py'))
# 判断是否为文件
print(os.path.isfile('os.path_test.py')) # True
# 判断是否为目录
print(os.path.isdir('os.path_test.py')) # False
# 判断是否为同一个文件
print(os.path.samefile('os.path_test.py', './os.path_test.py')) # True