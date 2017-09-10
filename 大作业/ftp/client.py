#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 18:49
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket,time,os,json,struct,hashlib
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))
def encrypt(password):
    md5=hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()

while True:
    userinfo={}
    user=input("user:").strip()
    if not user:continue
    userinfo["user"]=user
    pwd=input("password:").strip()
    if not pwd:continue
    userinfo["pwd"]=encrypt(pwd)
    client.send(json.dumps(userinfo).encode("utf-8"))
    json_bytes=client.recv(1024)
    result=json_bytes.decode("utf-8")
    if result!="True":
        print("username or password error,please re-enter")
        continue
    while True:
        msg=input(">>")
        if not msg:continue
        if msg in ["ls","dir"]:
            client.send(msg.encode("utf-8"))
            client_msg=client.recv(8096)
            print(client_msg.decode("utf-8"))
        if "put" in msg:
            fileinfo={}
            client.send(msg.encode("utf-8"))
            cmd,filename=msg.split(" ")
            if os.path.isfile(filename):
                fileinfo["filename"]=filename
                fileinfo["filesize"]=os.path.getsize(filename)
                json_data=json.dumps(fileinfo)
                header_bytes=json_data.encode("utf-8")
                json_header=struct.pack("i",len(header_bytes))
                client.send(json_header)
                client.send(header_bytes)
                f=open(filename,"rb")
                for line in f:
                    client.send(line)
            else:
                fileinfo["error"]="file %s on server does not exist"%filename
                print(fileinfo.get("error"))
    else:
        client.send(msg.encode("utf-8"))
        header_size=client.recv(4)[0]
        header_info=client.recv(header_size)
        dic_json=json.loads(header_info.decode("utf-8"))
        if dic_json.get("error"):
            print(dic_json.get("error"))
        else:
            local_size=0
            total_size=dic_json.get("filesize")
            print("total_size%s"%total_size)
            fn=dic_json["filename"]+"01"
            file=open(fn,"wb")
            while local_size<total_size[0]:
                data=client.recv(8096)
                local_size+=len(data)
                file.write(data)

