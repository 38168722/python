#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
def handle_request(client):
    buf=client.recv(1024)
    print("传过来的是啥",buf)
    print("是啥类型",type(buf))
    print("只取指定",buf.get("Referer"))
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    client.send("<h1 style='color:red'>Hello, yuan</h1>".encode("utf8"))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost",8088))
    server.listen(5)

    while True:
        print("starting server...")
        connection,address=server.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()