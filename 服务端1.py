import socket


server = socket.socket()

server.bind(('192.168.15.29',8081))

server.listen(5)

while 1:
    conn,addr = server.accept()
    # 字节类型
    while 1:
        data = conn.recv(1024)
        if data == b'exit':
            break
        response = data +b'great'
        conn.send(response)

    conn.close()
