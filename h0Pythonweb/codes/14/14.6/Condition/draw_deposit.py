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
import threading
import Account

#  定义一个函数，模拟重复max次执行取钱操作
def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)
#  定义一个函数，模拟重复max次执行存款操作
def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)
# 创建一个账户
acct = Account.Account("1234567" , 0)
# 创建、并启动一个“取钱”线程
threading.Thread(name="取钱者", target=draw_many, 
    args=(acct, 800, 100)).start()
# 创建、并启动一个“存款”线程
threading.Thread(name="存款者甲", target=deposit_many, 
    args=(acct , 800, 100)).start();
threading.Thread(name="存款者乙", target=deposit_many, 
    args=(acct , 800, 100)).start()
threading.Thread(name="存款者丙", target=deposit_many, 
    args=(acct , 800, 100)).start()
