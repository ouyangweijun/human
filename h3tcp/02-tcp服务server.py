# -*- coding:utf-8 -*-
# Author:oulen

"""
TCP demo
"""

import socket

def main():
    """创建TCP套接字"""

    # 1.创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定服务器相关信息
    tcp_server_socket.bind(("192.168.50.18",7788))
    tcp_server_socket.listen(128)


    # 3.提示用户输入数据
    # 4.接收数据、
    client_socket,clientAddr=tcp_server_socket.accept()
    print(clientAddr)

    recv_msg=client_socket.recv(1024)
    # 接收数据打印
    print('接收到的数据是%s' %(recv_msg.decode('gbk')))
    # 还送一部分数据给客户端
    client_socket.send('oueln send'.encode('gbk'))
    # 5.关闭套接字
    tcp_server_socket.close()



if __name__ == '__main__':
    main()