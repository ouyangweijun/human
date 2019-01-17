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

# 创建socket对象
s = socket.socket()
# 将socket绑定到本机IP和端口
s.bind(('192.168.1.88', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
# 每当接收到客户端socket的请求时，该方法返回对应的socket和远程地址
skt, addr = s.accept()
skt.send("服务器的第一行数据".encode('utf-8'))
skt.send("服务器的第二行数据".encode('utf-8'))
# 关闭socket的输出，表明输出数据已经结束
skt.shutdown(socket.SHUT_WR)
while True:
    # 从socket读取数据
    line = skt.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
skt.close()
s.close()
