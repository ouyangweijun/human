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
import socket, threading, CrazyitDict,CrazyitProtocol

from server_thread import server_target
SERVER_PORT = 30000
# 使用CrazyitDict来保存每个客户名字和对应socket之间的对应关系
clients = CrazyitDict.CrazyitDict()
# 创建socket对象
s = socket.socket()
try:
    # 将socket绑定到本机IP和端口
    s.bind(('192.168.1.88', SERVER_PORT))
    # 服务端开始监听来自客户端的连接
    s.listen()
    # 采用死循环来不断地接收来自客户端的请求
    while True:
        # 每当接收到客户端socket的请求时，该方法返回对应的socket和远程地址
        c, addr = s.accept()
        threading.Thread(target=server_target, args=(c, clients)).start()
# 如果抛出异常
except :
    print("服务器启动失败，是否端口%d已被占用？" % SERVER_PORT)
