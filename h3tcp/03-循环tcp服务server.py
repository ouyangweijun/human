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

    while True:
        # 3.提示用户输入数据
        # 4.接收数据、
        client_socket,clientAddr=tcp_server_socket.accept()
        print(clientAddr)

        while True:
            #循环为这客户端接收数据
            recv_msg=client_socket.recv(1024)
            # 接收数据打印
            print('接收到的数据是%s' %(recv_msg.decode('gbk')))

            # 如果recv解堵塞，那么有两种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close 导致关闭
            if recv_msg:
                 # 还送一部分数据给客户端
                 client_socket.send('oueln send'.encode('gbk'))
            else:
                break


        # 5.关闭套接字 关闭accept 返回的套接字，意味着不会再为新的客户端服务
        client_socket.close()
        print('为这客户端服务完毕')
    # 关闭全部socket,如果将监听套接字关闭，那么导致不能等待新客户端的到来，即ssss.acccept，就会失败
    tcp_server_socket.close()



if __name__ == '__main__':
    main()