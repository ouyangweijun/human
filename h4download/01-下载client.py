# -*- coding:utf-8 -*-
# Author:oulen

"""
下载文件deom
"""
import socket
def main():
    """下载文件demo"""

    # 1.创建套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.获取服务器信息
    dest_ip="192.168.50.18"
    dest_port=7788

    # 3.链接服务器
    tcp_socket.connect((dest_ip,dest_port))

    # 4.将文件发送到服务器
    download_file_name=input("输入想要下载文件名字:")

    # 5.将文件名字存到服务器
    tcp_socket.send(download_file_name.encode('gbk'))

    # 6.接收文件中的数据
    recv_data=tcp_socket.recv(1024*1024)  # 1024 ->1K 1024*1024....0->1K*1024=1M 1024*1024*1024--->1G
    # 7.保存文件数据到一个文件中

    if recv_data:
        with open("[新]"+download_file_name,"wb") as f:
            f.write(recv_data)

    # 8.关闭套接字
    tcp_socket.close()



if __name__ == '__main__':
    main()