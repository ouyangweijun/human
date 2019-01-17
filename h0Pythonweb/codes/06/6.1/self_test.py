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
    def test(self):
        print('self参数: ', self)
        
u = User()
# 以方法形式调用test()方法
u.test() # <__main__.User object at 0x00000000021F8240>
# 将User对象的test方法赋值给foo变量
foo = u.test
# 通过foo变量（函数形式）调用test()方法。
foo() # <__main__.User object at 0x00000000021F8240>
        
    