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
f = open('y.txt', 'wb+')
# os.linesep代表当前操作系统上的换行符
f.write(('我爱Python' + os.linesep).encode('utf-8'))
f.writelines((('土门壁甚坚，'+ os.linesep).encode('utf-8'),
    ('杏园度亦难。'+ os.linesep).encode('utf-8'),
    ('势异邺城下，'+ os.linesep).encode('utf-8'),
    ('纵死时犹宽。'+ os.linesep).encode('utf-8')))