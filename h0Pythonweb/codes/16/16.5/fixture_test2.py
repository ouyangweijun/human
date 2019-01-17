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
import unittest

from hello import *

class TestHello(unittest.TestCase):
    # 测试say_hello函数
    def test_say_hello(self):
        self.assertEqual(say_hello() , "Hello World.")
    # 测试add函数
    def test_add(self):
        self.assertEqual(add(3, 4) , 7)
        self.assertEqual(add(0, 4) , 4)
        self.assertEqual(add(-3, 0) , -3)
    @classmethod
    def setUpClass(cls):
        print('\n====执行setUpClass在类级别模拟初始化固件====')
    @classmethod
    def tearDownClass(cls):
        print('\n====调用tearDownClass在类级别模拟销毁固件====')
