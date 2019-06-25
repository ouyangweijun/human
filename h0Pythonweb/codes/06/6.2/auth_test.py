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
def auth(fn):
    def auth_fn(*args): 
        # 用一条语句模拟执行权限检查
        print("----模拟执行权限检查----")
        # 回调要装饰的目标函数
        fn(*args)
    return auth_fn
@auth
def test(a, b):
    print("执行test函数,参数a: %s, 参数b: %s" % (a, b))
# 调用test()函数,其实是调用装饰后返回的auth_fn函数
test(20, 15)
