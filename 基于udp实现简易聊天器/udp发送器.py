'''
@Date         : 2020-11-17 16:19:22
@LastEditors  : Pineapple
@LastEditTime : 2020-11-18 08:43:54
@FilePath     : /NetworkProgramming/udp1.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''
from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收的地址
# '172.23.212.225' 表示目标ip地址
# 8080表示目的端口
dest_addr = ('', 10240)

# 绑定端口
local_addr = ('', 10241)
udp_socket.bind(local_addr)

while True:
    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据: ")

    # 4. 发送数据到指定电脑的指定程序中
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    if send_data == 'exit':
        break

# 5. 关闭套接字
udp_socket.close()
