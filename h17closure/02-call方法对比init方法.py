#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-05 10:52
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 02-call方法对比init方法.py
# @Desc     : call 方法和init 方法

#__init__应该大家都知道，还是说一下，就是类的构造器，初始化一个类（创建一个类的实例）

class Student(object):

    def __init__(self, name):
        self.name = name


#调用的时候是这样的

#>> > a = Student('jack')
#>> > a.name
#'jack'

#__call__的话，它的作用是可以让
#一个类的实例像函数一样被调用，如
#可以像函数一样调用上面的a(‘jack2’)，相当于a.__call__(‘jack2’)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, name):
        self.name = name


#现在演示一下

#>> > a = Student('jack')
#>> > a.name
#'jack'
#>> > a('jack2’)
#       >> > a.name
#‘jack2
#'

#那么__call__的作用是什么呢？
#__call__ 在那些类的实例经常改变状态的时候会非常有效。调用这个实例是一种改变这个对象状态的直接和优雅的做法。用一个实例来表达最好不过了。
#嗯，没错就是

#1.
#为了让代码更优雅和直接

#2.
#方便改变实例中的一些变量（大部分应该改变状态）

