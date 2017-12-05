#!/usr/bin/env python
# -*- coding: utf-8 -*-
def login(environ):
    with open("template/login.html","rb") as f:
        data=f.read()
    return data

def auth(environ):
    print("QUERY_STRING",environ.get("QUERY_STRING"))
    useron,pwdon=environ.get("QUERY_STRING").split("&")
    _,user=useron.split("=")
    _,pwd=pwdon.split("=")
    import pymysql
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd="123456",db="auto")
    cur=conn.cursor()
    SQL="select * from user where name=%s and password =%s"
    cur.execute(SQL,[user,pwd])
    if cur.fetchone():
        with open("template/backend.html","r") as f:
            data=f.read()
        data=data%user
        return data.encode("utf8")
    else:
        with open("template/login.html","rb") as f:
            data=f.read()
        return data

def reg(environ):
    with open("template/reg.html","rb") as f:
        data = f.read()
    return data

def zhuce(environ):
    print("QUERY_STRING",environ.get("QUERY_STRING"))
    useron,pwdon,acpwdon=environ.get("QUERY_STRING").split("&")
    _,user=useron.split("=")
    _,pwd=pwdon.split("=")
    _,acpwd=acpwdon.split("=")
    if pwd!=acpwd:
        return b"password error please retry input"
    import pymysql
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd="123456",db="auto")
    cur=conn.cursor()
    SQL="insert into user(name,password)values(%s,%s)"
    ret=cur.execute(SQL,[user,pwd])
    print("ret等于多少==",ret)
    conn.commit()
    with open("template/backend.html","r") as f:
        data=f.read()
    data=data%user
    return data.encode("utf8")

