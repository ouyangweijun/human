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
import re

python_set = set(re.findall('[^,\.\s]+', input('学习Python的学员: ')))
java_set = set(re.findall('[^,\.\s]+', input('学习Java的学员: ')))
print(python_set)
print(java_set)
inter = python_set & java_set
print('既学Python又学Java的学员:', inter)
print('既学Python又学Java的学员有%d人' % len(inter))