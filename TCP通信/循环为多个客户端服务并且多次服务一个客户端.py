'''
@Date         : 2020-11-19 20:43:17
@LastEditors  : Pineapple
@LastEditTime : 2020-11-19 22:28:22
@FilePath     : /NetworkProgramming/循环为多个客户端服务并且多次服务一个客户端.py
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

    # 循环等待客户端
    while True:
        print('等待一个新的客户端的到来...')
        # 4. accept等待客户端的链接
        client_socket, client_addr = tcp_server_socket.accept()
        print(f'新的客户端到来: {client_addr}')

        # 循环为同一个客户端服务多次
        while True:
            # 接收客户端法从过来的请求
            try:
                recv_data = client_socket.recv(1024)
                print(f'客户端发送过来的请求是: {recv_data.decode("utf-8")}')
                # 如果recv解堵塞, 那么有两种方式:
                # 1. 客户端发送过来数据
                # 2. 客户端调用close
                client_socket.send('hahaha'.encode('utf-8'))
            # 如果客户端输入exit关闭连接, 则抛出异常退出服务
            except ConnectionResetError:
                break

        # 关闭客户端服务
        client_socket.close()
        print('已经为这个客户端服务完毕\n')

    # 关闭服务端
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
