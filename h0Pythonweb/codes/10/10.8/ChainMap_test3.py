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
from collections import ChainMap
import os, argparse
# 定义默认参数
defaults = {'color': '蓝色', 'user': 'yeeku'}
# 创建程序参数解析器
parser = argparse.ArgumentParser()
# 为参数解析器添加-u（--user）和-c（--color）参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
# 解析运行程序的参数
namespace = parser.parse_args()
# 将程序参数转换成dict
command_line_args = {k:v for k, v in vars(namespace).items() if v}
# 将command_line_args(解析程序参数而来)、os.environ(环境变量)、defaults链成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
# 获取color对应的value
print(combined['color'])
# 获取user对应的value
print(combined['user'])
# 获取PYTHONPATH对应的value
print(combined['PYTHONPATH'])