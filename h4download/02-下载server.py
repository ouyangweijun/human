# -*- coding:utf-8 -*-
# Author:oulen

"""
TCP demo
"""

import socket

def send_file_2_client(client_socket,clientAddr):
    """发送文件给客户端"""
    # 1.接收客户端想要下载的文件名称
    file_name=client_socket.recv(1024).decode('gbk')   # 1024 ->1K 1024*1024....0->1K*1024=1M 1024*1024*1024--->1G
    # 接收数据打印
    print('客户端（%s）需要下载的文件是：%s' %(str(clientAddr),file_name))

    file_content=None
    # 2.打开这个文件，读取数据   with 的情况下是文件存在
    try:
        f=open(file_name,'rb')
        file_content=f.read()
        f.close()
    except Exception as ret:
        print("没有想要下载的文件%s" % file_name)

    # 3.发送文件的数据给客户端
    if file_content:
        client_socket.send(file_content)
    if file_content == None:
        print('发送失败')



    # # 还送一部分数据给客户端
    # client_socket.send('oueln send'.encode('gbk'))


def main():
    """创建TCP套接字"""

    # 1.创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定服务器相关信息
    tcp_server_socket.bind(("192.168.50.18",7788))
    tcp_server_socket.listen(128)  # 监听的客户端数量


    # 3.提示用户输入数据
    # 4.接收数据
    while True:
        client_socket,clientAddr=tcp_server_socket.accept()

        send_file_2_client(client_socket,clientAddr)

        # 5.关闭套接字
        client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()