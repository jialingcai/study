from geventwebsocket.server import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
from flask import Flask, request, render_template
import json


app = Flask(__name__)
user_socket_list = []  # 连接的用户数


@app.route("/ws")
def my_ws_func():
    user_socket = request.environ.get("wsgi.websocket")   # 获取WebSocket的连接信息
    user_socket_list.append(user_socket)
    print(user_socket)
    while 1:
        msg = user_socket.receive()  # 等待接收消息
        for us in user_socket_list:
            if us == user_socket:
                continue
            try:
                us.send(msg)
            except:
                continue


@app.route('/group_p')
def group_p():
    return render_template('group_p.html')


if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0",9527),application=app,handler_class=WebSocketHandler)
    http_server.serve_forever()
