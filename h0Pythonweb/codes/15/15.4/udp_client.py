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
import socket

PORT = 30000;
# 定义每个数据报的大小最大为4KB
DATA_LEN = 4096;
DEST_IP = "192.168.1.88";
# 通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 不断地读取键盘输入
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    data = line.encode('utf-8')
    # 发送数据报
    s.sendto(data, (DEST_IP, PORT))
    # 读取socket中的数据
    data = s.recv(DATA_LEN)
    print(data.decode('utf-8'))
s.close()
