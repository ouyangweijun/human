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
class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
    def validLogin (self):
        print('验证%s的登录' % self.name)        
u = User('crazyit', 'leegang')
# 判断u.name是否包含__call__方法，即判断是否可调用
print(hasattr(u.name, '__call__')) # False
# 判断u.passwd是否包含__call__方法，即判断是否可调用
print(hasattr(u.passwd, '__call__')) # False
# 判断u.validLogin是否包含__call__方法，即判断是否可调用
print(hasattr(u.validLogin, '__call__')) # True

# 定义Role类
class Role:
    def __init__ (self, name):
        self.name = name
    # 定义__call__方法
    def __call__(self):
        print('执行Role对象')
r = Role('管理员')
# 直接调用Role对象，就是调用该对象的__call__方法
r()

def foo ():
    print('--foo函数--')
# 下面示范了2种方式调用foo()函数
foo()
foo.__call__()
