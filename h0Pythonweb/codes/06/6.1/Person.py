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
class Person :
    '这是一个学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'
    def __init__(self, name = 'Charlie', age=8):
        # 下面为Person对象增加2个实例变量
        self.name = name
        self.age = age
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
help(Person)
# 调用Person类的构造方法，返回一个Person对象
# 将该Person对象赋给p变量
p = Person()
# 输出p的name、age实例变量
print(p.name, p.age)  # Charlie 8
# 访问p的name实例变量，直接为该实例变量赋值
p.name = '李刚'
# 调用p的say()方法，声明say()方法时定义了2个形参
# 但第一个形参（self）是自动绑定的，因此调用该方法只需为第二个形参指定一个值
p.say('Python语言很简单，学习很容易！')
# 再次输出p的name、age实例变量
print(p.name, p.age)  # 李刚 8

# 为p对象增加一个skills实例变量
p.skills = ['programming', 'swimming']
print(p.skills)
# 删除p对象的name实例变量
del p.name
# 再次访问p的name实例变量
#print(p.name)  # AttributeError

# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对p的foo方法赋值（动态绑定方法）
p.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
p.foo(p)  # ①

# 使用lambda表达式为p对象的bar方法赋值（动态绑定方法）
p.bar = lambda self: print('--lambda表达式--', self)
p.bar(p) # ②

def intro_func(self, content):
    print("我是一个人，信息为：%s" % content)
# 导入MethodType
from types import MethodType
# 使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为p
p.intro = MethodType(intro_func, p)
# 第一个参数已经绑定了，无需传入
p.intro("生活在别处")
