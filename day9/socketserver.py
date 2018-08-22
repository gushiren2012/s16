import socket
import select

ip_add = ('127.0.0.1', 9000)
sk = socket.socket()
sk.bind(ip_add)
sk.listen(5)
inputs = [sk,]
outputs = []

while True:
    rlist, wlist,e = select.select(inputs, outputs,[],1)
    print(len(inputs), len(rlist), len(wlist), len(outputs))
    # 监听sk(服务器端)对象，如果sk对象发生变化，表示有客户端来链接了，此时rlist值为【sk】
    # 监听conn对象，如果conn发生变化，表示客户端有新消息发送过来了，此时rlist的值为【客户端】
    for r in rlist:
        if r == sk:
            # 新客户端来链接
            print(r)
            conn, addr = r.accept()
            # conn是什么？其实也是socket对象
            inputs.append(conn)
            conn.sendall(bytes('hello',encoding='utf-8'))
        else:
            # 是以存在的conn对象,给我发消息了
            try:
                ret = r.recv(1024)
                # r.sendall(ret)
                if not ret:
                    raise Exception('断开链接')
                else:
                    outputs.append(r)
            except Exception as e:
                inputs.remove(r)
    # 所有给我发过消息的人
    for w in wlist:
        w.sendall(bytes('response',encoding='utf-8'))
        outputs.remove(w)