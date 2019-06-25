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

class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        # 定义代表是否已经存钱的旗标
        self._flag = False

    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁,相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            # 如果self._flag为假，表明账户中还没有人存钱进去，取钱方法阻塞
            if not self._flag:
                self.cond.wait()
            else:
                # 执行取钱操作
                print(threading.current_thread().name 
                    + " 取钱:" +  str(draw_amount))
                self._balance -= draw_amount
                print("账户余额为：" + str(self._balance))
                # 将标识账户是否已有存款的旗标设为False
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用finally块来释放锁
        finally:
            self.cond.release()
    def deposit(self, deposit_amount):
        # 加锁,相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            # 如果self._flag为真，表明账户中已有人存钱进去，存钱方法阻塞
            if self._flag:            # ①
                self.cond.wait()
            else:
                # 执行存款操作
                print(threading.current_thread().name\
                    + " 存款:" +  str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为：" + str(self._balance))
                # 将表示账户是否已有存款的旗标设为True
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用finally块来释放锁
        finally:
            self.cond.release()