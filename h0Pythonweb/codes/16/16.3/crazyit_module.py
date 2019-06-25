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
def square (x):
    '''
    一个用于计算平方的函数

    例如
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-3)
    9
    >>> square(0)
    0
    '''
#    return x * 2 # ①、故意写错的
    return x ** 2 # 修改正确

class User:
    '''
    定义一个代表用户的类，该类包含如下两个属性：
    name - 代表用户的名字
    age - 代表用户的年龄

    例如
    >>> u = User('fkjava', 9)
    >>> u.name
    'fkjava'
    >>> u.age
    9
    >>> u.say('i love python')
    'fkjava说: i love python'
    '''
    def __init__(self, name, age):
#        self.name = 'fkit' # ②、故意写错的
        self.name = name # 修改正确
        self.age = age
    def say(self, content):
        return self.name + '说: ' + content
if __name__=='__main__':
    import doctest
    doctest.testmod()