'''
@Date         : 2020-11-19 19:27:55
@LastEditors  : Pineapple
@LastEditTime : 2020-11-19 22:06:19
@FilePath     : /NetworkProgramming/tcp_server.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''
from socket import *


def main():
    # 1. 创建tcp套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 2. 绑定ip和port
    tcp_server_socket.bind(('', 7890))

    # 3. listen设置成被动套接字
    tcp_server_socket.listen(128)
    print('----1----')

    # 4. accept等待客户端的链接
    # 如果有新的客户端链接服务器, 那么产生一个新的套接字专门为这个客户端服务
    # client_socket用来为这个客户端服务
    # tcp_server_socket就会闲下来专门等待其他新客户端链接
    client_socket, client_addr = tcp_server_socket.accept()
    print('----2----')
    print(client_addr)

    # 接收客户端法从过来的请求
    recv_data = client_socket.recv(1024)
    print(recv_data)

    # 回送数据给客户端
    client_socket.send('hahaha'.encode('utf-8'))

    # 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
