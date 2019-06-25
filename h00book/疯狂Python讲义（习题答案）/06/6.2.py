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
from student import Student

contacts = [Student('孙悟空', 500, 'MALE', '02028309358',
    '灵台方寸山', 'sun@crazyit.org'),
     Student('牛魔王', 650, 'MALE', '02028309378',
    '积雷山摩云洞', 'niu@crazyit.org'),
    Student('白骨精', 23, 'MALE', '13699881122',
    '白骨岭', 'bai@crazyit.org'),
    Student('猪八戒', 500, 'MALE', '13588889999',
    '福临山山云栈洞', 'zhu@crazyit.org')]
def find_by_name(name):
    return [x for x in contacts if name in x.name]
def find_by_email(email):
    return [x for x in contacts if email in x.email]
def find_by_address(address):
    return [x for x in contacts if address in x.address]

if __name__ == '__main__':
    t = input('请输入查找的方式, 名字(n), Email(e), 地址(a): ')
    k = input('请输入查找的关键字: ')
    if t == 'n':
        print(find_by_name(k))
    elif t == 'e':
        print(find_by_email(k))
    elif t == 'a':
        print(find_by_address(k))
    else:
        print('输入有误!')   
        
    

    