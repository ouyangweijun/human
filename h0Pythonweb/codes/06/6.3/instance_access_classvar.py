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
class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'
    def info (self):
        print('info方法中: ', self.item)
        print('info方法中: ', self.date)

rc = Record()
print(rc.item) # '鼠标'
print(rc.date) # '2016-06-16'
rc.info()
    
# 修改Record类的两个类变量
Record.item = '键盘'
Record.date = '2016-08-18'
# 调用info()方法
rc.info()