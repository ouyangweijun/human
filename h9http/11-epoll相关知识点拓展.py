#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-03 08:14
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 11-epoll相关知识点拓展.py
# @Desc     : epoll相关知识点拓展

# Web静态服务器-6-epoll
# IO 多路复用
# 就是我们说的select，poll，epoll，有些地方也称这种IO方式为event driven IO。
#
# select/epoll的好处就在于单个process就可以同时处理多个网络连接的IO。
#
# 它的基本原理就是select，poll，epoll这个function会不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程。
#
# epoll简单模型
import socket
import select

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# 绑定本机信息
s.bind(("",7788))

# 变为被动
s.listen(10)

# 创建一个epoll对象
epoll = select.epoll()

# 测试，用来打印套接字对应的文件描述符
# print(s.fileno())
# print(select.EPOLLIN|select.EPOLLET)

# 注册事件到epoll中
# epoll.register(fd[, eventmask])
# 注意，如果fd已经注册过，则会发生异常
# 将创建的套接字添加到epoll的事件监听中
epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

# 循环等待客户端的到来或者对方发送数据
while True:

    # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
    epoll_list = epoll.poll()

    # 对事件进行判断
    for fd, events in epoll_list:

        # print fd
        # print events

        # 如果是socket创建的套接字被激活
        if fd == s.fileno():
            new_socket, new_addr = s.accept()

            print('有新的客户端到来%s' % str(new_addr))

            # 将 conn 和 addr 信息分别保存起来
            connections[new_socket.fileno()] = new_socket
            addresses[new_socket.fileno()] = new_addr

            # 向 epoll 中注册 新socket 的 可读 事件
            epoll.register(new_socket.fileno(), select.EPOLLIN|select.EPOLLET)

        # 如果是客户端发送数据
        elif events == select.EPOLLIN:
            # 从激活 fd 上接收
            recvData = connections[fd].recv(1024).decode("utf-8")

            if recvData:
                print('recv:%s' % recvData)
            else:
                # 从 epoll 中移除该 连接 fd
                epoll.unregister(fd)

                # server 侧主动关闭该 连接 fd
                connections[fd].close()
                print("%s---offline---" % str(addresses[fd]))
                del connections[fd]
                del addresses[fd]
# 说明
# EPOLLIN （可读）
# EPOLLOUT （可写）
# EPOLLET （ET模式）
# epoll对文件描述符的操作有两种模式：LT（level trigger）和ET（edge trigger）。LT模式是默认模式，LT模式与ET模式的区别如下：
#
# LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。下次调用epoll时，会再次响应应用程序并通知此事件。
#
# ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。