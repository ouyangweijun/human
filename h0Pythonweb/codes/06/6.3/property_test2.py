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
class User :
    def __init__ (self, first, last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + ',' + self.last
    def setfullname(self, fullname):
        first_last = fullname.rsplit(',');
        self.first = first_last[0]
        self.last = first_last[1]
    # 使用property()函数定义fullname属性，只传入2个参数
    # 该属性是一个读写属性，但不能删除
    fullname = property(getfullname, setfullname)
u = User('悟空', '孙')
# 访问fullname属性
print(u.fullname)
# 对fullname属性赋值
u.fullname = '八戒,朱'
print(u.first)
print(u.last)
