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
import time, socket, threading, os
 
# 定义本机IP地址
SENDERIP = '192.168.1.88'
# 定义本地端口
SENDERPORT = 30000
# 定义本程序的多点广播IP地址
MYGROUP = '230.0.0.1'
# 通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 将该socket绑定到0.0.0.0的虚拟IP
s.bind(('0.0.0.0', SENDERPORT))     # ①
# 设置广播消息的TTL（Time-To-Live）
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
# 设置允许多点广播使用相同的端口
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 将socket进入广播组
status = s.setsockopt(socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))
# 定义从socket读取数据的方法
def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print("信息: ", data.decode('utf-8'))
# 以read_socket作为target启动多线程
threading.Thread(target=read_socket, args=(s, )).start()
# 采用循环不断读取键盘输入，并输出到socket中
while True:
    line = input('')
    if line is None or line == 'exit':
        break
        os._exit(0)
    # 将line输出到socket中
    s.sendto(line.encode('utf-8'), (MYGROUP, SENDERPORT))
