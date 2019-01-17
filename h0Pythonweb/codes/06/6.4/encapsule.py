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
    def __hide(self):
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3～8之间')
        self.__name = name
    name = property(getname, setname)
    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在18在70之间')
        self.__age = age
    def getage(self):
        return self.__age
    age = property(getage, setage)
# 创建User对象
u = User()
# 对name属性赋值，实际上调用setname()方法
#u.name = 'fk' # 引发 ValueError: 用户名长度必须在3～8之间
u.name = 'fkit'
u.age = 25
print(u.name) # fkit
print(u.age) # 25

# 尝试调用隐藏的__hide()方法
#u.__hide()

# 调用隐藏的__hide()方法
u._User__hide()
# 对隐藏的__name属性赋值
u._User__name = 'fk'
# 访问User对象的name属性（实际上访问__name实例变量）
print(u.name)
