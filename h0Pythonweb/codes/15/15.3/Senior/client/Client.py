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
import socket, threading, CrazyitProtocol, os
from tkinter import simpledialog
import time

SERVER_PORT = 30000

# 定义一个读取键盘输入，并向网络发送的函数
def read_send(s):
    # 采用死循环不断地读取键盘输入
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        # 如果发送的信息中有冒号，且以//开头，则认为想发送私聊信息
        if ":" in line and line.startswith("//"):
            line = line[2:]
            s.send((CrazyitProtocol.PRIVATE_ROUND 
                + line.split(":")[0] + CrazyitProtocol.SPLIT_SIGN
                + line.split(":")[1] + CrazyitProtocol.PRIVATE_ROUND).encode('utf-8'))
        else:
            s.send((CrazyitProtocol.MSG_ROUND + line
                + CrazyitProtocol.MSG_ROUND).encode('utf-8'))
# 创建socket对象
s = socket.socket()
try:
    # 连接远程主机
    s.connect(('192.168.1.88', SERVER_PORT))
    tip = ""
    # 采用循环不断地弹出对话框要求输入用户名
    while True:
        user_name = input(tip + '输入用户名:\n')     # ①
        # 在用户输入的用户名前后增加协议字符串后发送
        s.send((CrazyitProtocol.USER_ROUND + user_name
            + CrazyitProtocol.USER_ROUND).encode('utf-8'))
        time.sleep(0.2)
        # 读取服务器端的响应
        result = s.recv(2048).decode('utf-8')
        if result is not None and result != '':
            # 如果用户名重复，则开始下次循环
            if result == CrazyitProtocol.NAME_REP:
                tip = "用户名重复！请重新"
                continue
            # 如果服务器端返回登录成功，则结束循环
            if result == CrazyitProtocol.LOGIN_SUCCESS:
                break
# 捕获到异常，关闭网络资源，并退出该程序
except:
    print("网络异常！请重新登录！")
    s.close()
    os._exit(1)
def client_target(s):
    try:
        # 不断地从socket中读取数据，并将这些数据打印输出
        while True:
            line = s.recv(2048).decode('utf-8')
            if line is not None:
                print(line)
            # 本例仅打印了从服务器端读到的内容。实际上，此处的情况可以更复杂：如
            # 果希望客户端能看到聊天室的用户列表，则可以让服务器端在每次有用户登
            # 录、用户退出时，将所有的用户列表信息都向客户端发送一遍。为了区分服
            # 务器端发送的是聊天信息，还是用户列表，服务器端也应该在要发送的信息
            # 前、后都添加一定的协议字符串，客户端则根据协议字符串的不同而进行不
            # 同的处理！
            # 更复杂的情况：
            # 如果两端进行游戏，则还有可能发送游戏信息，例如两端进行五子棋游戏，
            # 则需要发送下棋坐标信息等，服务器端同样在这些下棋坐标信息前、后添加
            # 协议字符串后再发送，客户端就可以根据该信息知道对手的下棋坐标。
    # 使用finally块来关闭该线程对应的socket
    finally:
        s.close()
# 启动客户端线程
threading.Thread(target=client_target, args=(s,)).start()
read_send(s)
