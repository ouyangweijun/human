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

# 以读写、创建方式打开文件
f = os.open('abc.txt', os.O_RDWR|os.O_CREAT)
# 写入文件内容
len1 = os.write(f, '水晶潭底银鱼跃，\n'.encode('utf-8'))
len2 = os.write(f, '清徐风中碧竿横。\n'.encode('utf-8'))
# 将文件指针移动到开始处
os.lseek(f, 0, os.SEEK_SET)
# 读取文件内容
data = os.read(f, len1 + len2)
# 打印读取到字节串
print(data)
# 将字节串恢复成字符串
print(data.decode('utf-8'))
os.close(f)