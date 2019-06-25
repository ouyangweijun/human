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
import multiprocessing
import time

class Account:
    # 定义构造器
    def __init__(self, account_no, balance, lock):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = lock

    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance
    # 提供一个进程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(multiprocessing.current_process().name\
                    + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(multiprocessing.current_process().name\
                    + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()
# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    print(account)
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount)

if __name__ == '__main__':
    lock = multiprocessing.RLock()
    # 创建一个账户
    acct = Account("1234567" , 900, lock)
    # 模拟两个进程对同一个账户取钱
    multiprocessing.Process(name='甲', target=draw , args=(acct , 800)).start()
    multiprocessing.Process(name='乙', target=draw , args=(acct , 800)).start()
    multiprocessing.Process(name='丙', target=draw , args=(acct , 800)).start()
