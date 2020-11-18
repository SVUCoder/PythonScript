'''
@Date         : 2020-11-17 20:28:24
@LastEditors  : Pineapple
@LastEditTime : 2020-11-17 21:21:55
@FilePath     : /NetworkProgramming/udp2.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''
from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定本地的相关信息, 如果一个网络程序不稳定, 则系统会随机分配
local_addr = ('', 7788)  # ip地址和端口号, ip一般不用写, 表示本机的任何一个ip
udp_socket.bind(local_addr)

while True:

    # 3. 等待接受对方发送的数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示最多接收1024个字节

    if recv_data[0] == b'exit':
        break

    # 4. 显示接收到的数据
    recv_msg = recv_data[0]  # 存储接收的数据
    recv_addr = recv_data[1]  # 存储发送放的地址信息
    print(str(recv_addr), recv_msg.decode('utf-8'))

# 5. 关闭套接字
udp_socket.close()
