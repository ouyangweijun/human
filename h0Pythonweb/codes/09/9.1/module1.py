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
'''
这是我们编写的第一个模块，该模块包含以下内容：
my_book：字符串变量
say_hi：简单的函数
User：代表用户的类
'''
print('这是module 1')
my_book = '疯狂Python讲义'
def say_hi(user):
    print('%s,您好，欢迎学习Python' % user)
class User:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('%s正在慢慢地走路' % self.name)
    def __repr__(self):
        return 'User[name=%s]' % self.name
          
        
# ===以下部分是测试代码===
def test_my_book ():
    print(my_book)
def test_say_hi():
    say_hi('孙悟空')
    say_hi(User('Charlie'))
def test_User():
    u = User('白骨精')
    u.walk()
    print(u)
# 当__name__为'__main__'（直接使用python运行该模块）时执行如下代码
if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_User()


    
