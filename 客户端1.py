import socket


sk = socket.socket()

sk.connect(('192.168.15.29', 8081))

while 1:
    name = input("请输入你的名字:")
    sk.send(name.encode('utf8'))

    if name == "exit":
        break

    response = sk.recv(1024)

    print(response.decode('utf8'))

sk.close()