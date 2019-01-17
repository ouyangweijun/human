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
import json

name = input('请输入您的名字: ')
while True:
    try:
        age = int(input('请输入您的年龄: '))
        break
    except:
        print('年龄需要您输入整数')
while True:
    try:
        height = float(input('请输入您的身高: '))
        break
    except:
        print('身高需要您输入浮点数')
with open('my.txt', 'w+') as f:
    json.dump({'name': name, 'age': age, 'height': height}, f)

with open('my.txt', 'r') as f:
    my_info = json.load(f)
    print(my_info['name'])
    print(my_info['age'])
    print(my_info['height'])