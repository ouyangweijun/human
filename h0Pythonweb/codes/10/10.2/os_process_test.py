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
# 运行平台上的cmd命令
os.system('cmd')
# 使用Excel打开g:\abc.xls文件
os.startfile('g:\\abc.xls')
os.spawnl(os.P_NOWAIT, 'E:\\Tools\\编辑工具\\Notepad++.7.5.6.bin.x64\\notepad++.exe', ' ')
# 使用python命令执行os_test.py程序
os.execl("D:\\Python\\Python36\\python.exe", " ", 'os_test.py', 'i') 
