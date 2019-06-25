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

# 判断当前目录的权限
ret = os.access('.', os.F_OK|os.R_OK|os.W_OK|os.X_OK)
print("os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:", ret)
# 判断os.access_test.py文件的权限
ret = os.access('os.access_test.py', os.F_OK|os.R_OK|os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)
