# !/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
ip_add = ('127.0.0.1',9000)
s = socket.socket()
s.connect(ip_add)
data = s.recv(1024)
print(data)

while True:
    send_data = input(">>>:")
    if send_data == 'exit': break
    if len(send_data) == 0: continue
    s.sendall(bytes(send_data,encoding='utf-8'))
    print(s.recv(1024))
s.close()