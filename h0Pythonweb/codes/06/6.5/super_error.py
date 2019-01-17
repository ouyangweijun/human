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
class Employee :
    def __init__ (self, salary):
        self.salary = salary
    def work (self):
        print('普通员工正在写代码，工资是:', self.salary)
class Customer:
    def __init__ (self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info (self):
        print('我是一个顾客，我的爱好是: %s,地址是%s' % (self.favorite, self.address))
# Manager继承了Employee、Customer
#class Manager (Employee, Customer):
class Manager (Customer, Employee):
    pass
#m = Manager(25000)
m = Manager('IT产品', '广州')
#m.work()  #①
m.info()  #②

        
    