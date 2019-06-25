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
class Student:
    ''' 描述学生的类'''
    def __init__(self, name, age, gender, phone, address, email):
        ''' 构造器 '''
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    def eat(self, food):
        ''' 吃 '''
        print('%s正在吃%s' % (self.name, food))

    def drink(self, drink):
        ''' 喝 '''
        print('%s正在喝%s' % (self.name, drink))        
        
    def play(self, sport, other):
        ''' 玩 '''
        print('我今年%s岁，正和%s玩%s' % (self.age, other, sport)) 

    def sleep(self):
        ''' 睡 '''
        print('%s正在%s睡觉' % (self.name, self.address)) 

    def __repr__(self):
        return 'Student(name=%s, age=%d, phone=%s, address=%s, email=%s)' % (self.name, self.age, self.phone, self.address, self.email)

if __name__ == '__main__':
    stu = Student('孙悟空', 500, 'MALE', '02028309358',
        '灵台方寸山', 'sun@crazyit.org')
    stu.eat('桃子')
    stu.drink('美酒')
    stu.play('棍子', '牛魔王')
    stu.sleep()
