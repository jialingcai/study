# study
创建websocket连接的方式
1.首先要引入第三方组件  genvent-websocket
2. 在组件中引入 from genventwebsocket.server import WSGIWebsocket 这里的意思是需要WSGI提供服务
                from geventwebsocket.handle import WebsocketHandler  这里是指ws请求到来以后的处理方式
                from geventwebsocket,websocket import Websocket  这里是指you语法提示
3. 因为我们是 基于Flask +gevenywebsocket 实现的聊天室功能 所以需要设置一个flask视图     

4.启动的时候 使用的是WSGIWebsocket服务了,不在是flask的启动方式了
    http_serv = WSGIServer(("0.0.0.0",9527),application=app,handler_class=WebSocketHandler)
    http_serv.serve_forever()