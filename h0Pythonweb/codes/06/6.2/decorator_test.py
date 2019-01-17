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
def funA(fn):
    print('A')
    fn() # 执行传入的fn参数
    return 'fkit'
'''
下面装饰效果相当于：funA(funB)，
funB将会替换（装饰）成该语句的返回值；
由于funA()函数返回fkit，因此funB就是fkit
'''
@funA
def funB():
    print('B')
print(funB) # fkit

def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))
    return bar
'''
下面装饰效果相当于：foo(my_test)，
my_test将会替换（装饰）成该语句的返回值；
由于foo()函数返回bar函数，因此funB就是bar
'''
@foo
def my_test(a):
    print("==my_test函数==", a)
# 打印my_test函数，将看到实际上是bar函数
print(my_test) # <function foo.<locals>.bar at 0x00000000021FABF8>
# 下面代码看上去是调用my_test()，其实是调用bar()函数
my_test(10)
my_test(6, 5)