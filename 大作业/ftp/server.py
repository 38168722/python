#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 18:48
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socket,random,os,time,struct,json,hashlib
from threading import Thread
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("127.0.0.1",8080))
server.listen(5)

def get_file_info(command):
    return os.popen(command).read()

def encrypt(password):
    md5=hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()

def auth_user(conn,addr):
    local_user=json.load(open("auth"))
    client_user=json.loads(conn.recv(1024).decode("utf-8"))
    if client_user["user"] in local_user and encrypt(local_user[client_user["user"]])==client_user["pwd"]:
        conn.send("True".encode("utf-8"))
    else:
        conn.send("False".encode("utf-8"))
def talk(conn,addr):
    auth_user(conn,addr)
    while True:
        client_msg=conn.recv(1024).decode("utf-8")
        if client_msg in ["ls","dir"]:
            command=get_file_info(client_msg)
            conn.send(command.encode("utf-8"))
        else:
            cmd,filename=client_msg.split(" ")
            if cmd=="get":
                fileinfo={}
                if os.path.isfile(filename):
                    fileinfo["filesize"]=os.path.getsize(filename),
                    fileinfo["filename"]=filename
                    json_data=json.dumps(fileinfo)
                    header_bytes=json_data.encode("utf-8")
                    json_header=struct.pack("i",len(header_bytes))
                    conn.send(json_header)
                    conn.send(header_bytes)
                    f=open(filename,"rb")
                    for line in f:
                        conn.send(line)
                else:
                    fileinfo["error"]="file %s on server does not exist"%filename
                    error_info=json.dumps(fileinfo).encode("utf-8")
                    json_header=struct.pack("i",len(error_info))
                    conn.send(json_header)
                    conn.send(error_info)
            if cmd=="put":
                struct_header=struct.unpack("i",conn.recv(4))[0]
                json_dic=json.loads(conn.recv(struct_header).decode("utf-8"))
                totalsize=json_dic.get("filesize")
                filename=json_dic.get("filename")+"001"
                localsize=0
                fn=open(filename,"wb")
                while localsize<totalsize:
                    data=conn.recv(8096)
                    localsize+=len(data)
                    fn.write(data)
        conn.close()

if __name__ == '__main__':
    while True:
        print("starting......")
        conn,addr=server.accept()
        Thread(target=talk,args=(conn,addr)).start()
    server.close()