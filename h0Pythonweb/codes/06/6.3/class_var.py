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
class Address :
    detail = '广州'
    post_code = '510660'
    def info (self):
        # 尝试直接访问类变量
#        print(detail) # 报错
        # 通过类来访问类变量
        print(Address.detail) # 输出 广州
        print(Address.post_code) # 输出 510660
# 通过类来访问Address类的类变量
print(Address.detail)
addr = Address()
addr.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()