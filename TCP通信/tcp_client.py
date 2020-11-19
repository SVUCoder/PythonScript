'''
@Date         : 2020-11-19 18:54:47
@LastEditors  : Pineapple
@LastEditTime : 2020-11-19 19:05:29
@FilePath     : /NetworkProgramming/tcp_client.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''
from socket import *


def main():
    # 1. 创建tcp套接字
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 2. 连接服务器
    server_ip = input('请输入要连接的服务器ip: ')
    server_port = int(input('请输入要连接的服务器port: '))
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr)

    # 3. 发送数据/接收数据
    send_data = input('请输入要发送的数据: ')
    tcp_client_socket.send(send_data.encode('utf-8'))

    # 4. 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
