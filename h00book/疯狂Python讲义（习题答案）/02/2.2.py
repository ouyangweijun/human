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
#算术运算符
num1 = 9 + 2
print("加:%d" % num1);
num2 = 9 - 2
print("减:%d" % num2);
num3 = 9 * 2
print("乘:%d" % num3);
num4 = 9 / 2
print("除:%d" % num4);
# 取整除
num5 = 9 // 2
print("取整除:%d" % num5);
# 取余数
num6 = 9 % 2
print("取余数:%d" % num6);
# 取次幂
num7 = 9 ** 2
print("取次幂:%d" % num7);

# 比较运算符
a = 7
b = 3
print("a == b: %s" % (a == b));
print("a != b: %s" % (a != b));
print("a > b: %s" % (a > b));
print("a < b: %s" % (a < b));
a = 3
print("a >= b: %s" % (a >= b));
print("a <= b: %s" % (a <= b));

# 逻辑运算符
# and(与)有一个表达式为False，则返回False
print("True and True: %s"%(True and True));
print("True and False: %s"%(True and False));
print("False and False: %s"%(False and False));
# or(或) 有一个表达式为True，则返回True
print("True or True: %s"%(True or True));
print("True or False: %s"%(True or False));
print("False or False: %s"%(False or False));
# not(或) 取反
print("not(True and True): %s"%(not(True and True)));
print("not(False and False): %s"%(not(False and False)));