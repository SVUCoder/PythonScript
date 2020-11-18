'''
@Date         : 2020-11-18 09:36:39
@LastEditors  : Pineapple
@LastEditTime : 2020-11-18 10:00:44
@FilePath     : /NetworkProgramming/udp4.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''
from socket import *


def send_msg(udp_socket, dest_addr):
    """发送数据"""
    msg = input('请输入要发送的信息: ')
    udp_socket.sendto(msg.encode('utf-8'), dest_addr)


def recv_msg(udp_socket):
    msg = udp_socket.recvfrom(1024)
    print(msg[0].decode('utf-8')+str(msg[1]))


def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    local_addr = ('', 10240)

    # 绑定端口号
    udp_socket.bind(local_addr)

    print('---xxx聊天器---\n')

    dest_ip = input('请输入要发送的ip: ')
    dest_port = int(input('请输入要发送的port: '))

    dest_addr = (dest_ip, dest_port)

    while True:
        print('请选择相应的功能: ')
        print('1: 发送数据')
        print('2: 接收数据')
        print('0: 退出程序')

        op = input('选择: ')

        if op == '1':
            send_msg(udp_socket, dest_addr)
        elif op == '2':
            recv_msg(udp_socket)
        elif op == '0':
            break

    udp_socket.close()


if __name__ == "__main__":
    main()
