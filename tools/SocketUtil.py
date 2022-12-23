
from core.Request import Request
from core.Response import Response

import socket

class SocketUtil:
    @staticmethod
    def getSocket(ip: str, port: int) -> socket:
        # 创建一个socket对象
        # AF_INET       = 服务器之间网络通信
        # SOCK_STREAM   = 流式socket , for TCP
        listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 添加Address
        listenSocket.bind((ip, port))

        # 设置超时时间
        # listenSocket.settimeout(100)

        # 设置最大连接数|开始监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
        listenSocket.listen(10)

        return listenSocket

    @staticmethod
    def getConn(listenSocket: socket, bufsize: int, isDecode="utf-8") -> Request:
        # 接受TCP连接并返回(conn,address)
        # conn      新的套接字对象, 可以用来接收和发送数据
        # address   连接客户端的地址
        conn, Address = listenSocket.accept()

        # 接受TCP套接字的数据, 数据以字符串形式返回
        # bufsize指定要接收的最大数据量
        # flag提供有关消息的其他信息, 通常可以忽略
        if isDecode == False: source = conn.recv(bufsize)
        else: source = conn.recv(bufsize).decode(encoding=isDecode)

        return Request(conn, source)

    def sendAll(request: Request, response: Response):
        request.conn.sendall(bytes(response.result(), "utf-8"))

    def close(listenSocket: socket):
        listenSocket.close()
