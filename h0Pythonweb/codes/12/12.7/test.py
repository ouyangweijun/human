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
import os, sys

# 打开文件
fd = os.open("f1.txt",os.O_RDWR|os.O_CREAT)

print(fd)

## 写入字符串
#ret = os.write(fd,"This is runoob.com site")
#
## 输入返回值
#print "写入的位数为: "
#print  ret
#
#print "写入成功"
#
## 关闭文件
#os.close(fd)
#print "关闭文件成功!!"