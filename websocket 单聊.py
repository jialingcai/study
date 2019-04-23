from geventwebsocket.server import WSGIServer  #我要WSGI为我提供服务
from geventwebsocket.handler import WebSocketHandler  # 遇到WSGI协议的时候的处理方法
from geventwebsocket.websocket import WebSocket  #语法提示


# 基于Flask +gevenywebsocket

from flask import Flask,request,render_template
import json

app = Flask(__name__)
user_socket_dict = {}


@app.route('/ws/<nickname>')
def my_ws_func(nickname):
    print(dir(request.environ))
    user_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    print(user_socket)
    user_socket_dict[nickname] = user_socket
    print(user_socket_dict)
    while 1:
        msg = user_socket.receive()  #等待接收客户端发送的消息
        print(msg)
        msg = json.loads(msg)  # 消息转成Dict
        to_user_socket = user_socket_dict.get(msg.get('to_user'))  # 获取要接收消息的那个人
        msg_json = json.dumps(msg)
        to_user_socket.send(msg_json) #发送消息


@app.route('/one_p')
def one_p():
    return render_template('one_p.html')

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9527),application=app,handler_class=WebSocketHandler)
    http_serv.serve_forever()