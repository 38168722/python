#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/4 16:01
# @Author  : Aries
# @Site    : 
# @File    : 员工信息管理2.py
# @Software: PyCharm

# coding = utf-8
import os
# 登录状态
user_state = {"username": None, "state": False}
# 用户数据
user_dict = {"egon": "111", "Alex": "222", "yuanhao": "333", "wupeiqi": "444"}


# 装饰器
def auth(func):
    def inner(*args, **kwargs):
        while not user_state["state"]:
            login(*args, **kwargs)
        re = func()
        return re

    return inner


# 登录验证操作
def login(*args, **kwargs):
    name = input("输入用户名:").strip()
    passwd = input("输入密码：").strip()
    if user_dict.get(name) and passwd == user_dict[name]:
        user_state["username"] = name
        user_state["state"] = True
        print("login successful")
    else:
        print("login Failed")


# 查询    例 ==》 select name, age where age>22  或 select * where job=IT 或  select * where phone like 133
@auth
def select():
    select_dict = {}
    input_str = input("输入查询语句==>").strip()
    element = [x.strip() for x in
               (input_str[input_str.index("select") + 6:input_str.index("where")]).strip().split(",")]
    a = input_str[input_str.index("where") + 5:].strip()
    symbol = [">", "<", "=", "like"]
    for x in symbol:
        if x in a:
            term = [i.strip() for i in a.split(x)]
            term.insert(0, x)
    try:
        with open("db.txt", encoding="utf-8") as f:
            for line in f:
                if len(line)!=1:
                    a = line.rstrip("\n").split(",")
                    select_dict["id"], select_dict["name"], select_dict["age"], select_dict["phone"], select_dict["job"] = a
                    term_out = []
                    if term[0] == "like":
                        if term[2] in select_dict[term[1]]:
                            if element[0] == '*':
                                print(line.strip("\n"))
                            else:
                                for x in element:
                                    term_out.append(select_dict[x])
                                print(",".join(term_out))
                    elif term[0] == ">":
                        if int(select_dict[term[1]]) > int(term[2]):
                            if element[0] == '*':
                                print(line.strip("\n"))
                            else:
                                for x in element:
                                    term_out.append(select_dict[x])
                                print(",".join(term_out))
                    elif term[0] == "<":
                        if int(select_dict[term[1]]) < int(term[2]):
                            if element[0] == '*':
                                print(line.strip("\n"))
                            else:
                                for x in element:
                                    term_out.append(select_dict[x])
                                print(",".join(term_out))
                    elif term[0] == "=":
                        if term[2].isdigit():
                            if int(select_dict[term[1]]) == int(term[2]):
                                if element[0] == '*':
                                    print(line.strip("\n"))
                                else:
                                    for x in element:
                                        term_out.append(select_dict[x])
                                    print(",".join(term_out))
                        else:
                            if select_dict[term[1]] == term[2]:
                                if element[0] == '*':
                                    print(line.strip("\n"))
                                else:
                                    for x in element:
                                        term_out.append(select_dict[x])
                                    print(",".join(term_out))
                else :
                    continue
        print("查询数据完成！\n")
    except :
        print("不知道哪里出错啦，赶紧抛出")


# 创建新员工记录   例 ==》 4,yuanhao,55,13370867894,work
@auth
def insert():
    input_str = input("输入新员工信息==>").strip()
    with open("db.txt", "a", encoding="utf-8") as f:
        f.seek(0,2)
        f.write("\n"+input_str)
    print("添加新员工完成！\n")


# 删除指定员工记录  例 ：==》 1
@auth
def delete():
    input_str = input("输入删除id==>").strip()
    id_in = {"state": False}
    try:
        with open("db.txt", "r", encoding="utf-8") as f1:
            with open("db1.txt", "w", encoding="utf-8")as f2:
                for line in f1:
                    line_list = line.split(",")
                    if input_str == line_list[0].strip():
                        id_in["state"] = True
                        continue
                    else:
                        f2.write(line)
        os.remove("db.txt")
        os.rename("db1.txt", "db.txt")
        print("删除数据成功！\n") if id_in["state"] else print("删除失败，id=%s不存在\n" % input_str)
    except:
        print("不知道哪里出错啦，赶紧抛出")


# 修改员工信息      例 ==》 set name = egon where age>23
@auth
def update():
    input_str = input("输入修改信语句==>").strip()
    element = [x.strip() for x in (input_str[input_str.index("set") + 3:input_str.index("where")]).strip().split("=")]
    a = input_str[input_str.index("where") + 5:].strip()
    symbol = [">", "<", "=", "like"]
    for x in symbol:
        if x in a:
            term = [i.strip() for i in a.split(x)]
            term.insert(0, x)
    update_dict = {}
    try:
        with open("db.txt", encoding="utf-8") as fr:
            with open("db2.txt", "w", encoding="utf-8") as fw:
                for line in fr:
                    if len(line)!=1:
                        a = line.rstrip("\n").split(",")
                        update_dict["id"], update_dict["name"], update_dict["age"], update_dict["phone"], update_dict["job"] = a
                        if term[0] == "like":
                            if term[2] in update_dict[term[1]]:
                                update_dict[element[0]] = element[1]
                                fw.write(",".join(update_dict.values()) + "\n")
                            else:
                                fw.write(",".join(update_dict.values()) + "\n")
                        elif term[0] == ">":
                            if int(update_dict[term[1]]) > int(term[2]):
                                update_dict[element[0]] = element[1]
                                fw.write(",".join(update_dict.values()) + "\n")
                            else:
                                fw.write(",".join(update_dict.values()) + "\n")
                        elif term[0] == "<":
                            if int(update_dict[term[1]]) < int(term[2]):
                                update_dict[element[0]] = element[1]
                                fw.write(",".join(update_dict.values()) + "\n")
                            else:
                                fw.write(",".join(update_dict.values()) + "\n")
                        elif term[0] == "=":
                            if term[2].isdigit():
                                if int(update_dict[term[1]]) == int(term[2]):
                                    update_dict[element[0]] = element[1]
                                    fw.write(",".join(update_dict.values()) + "\n")
                                else:
                                    fw.write(",".join(update_dict.values()) + "\n")
                            else:
                                if update_dict[term[1]] == term[2]:
                                    update_dict[element[0]] = element[1]
                                    fw.write(",".join(update_dict.values()) + "\n")
                                else:
                                    fw.write(",".join(update_dict.values()) + "\n")
                    else:
                        continue
        os.remove("db.txt")
        os.rename("db2.txt", "db.txt")
        print("修改数据完成！\n")
    except:
        print("不知道哪里出错啦，赶紧抛出")


func_dict={"select":select,"insert":insert,"delete":delete,"update":update}
info ='''===================
    查询---select
    插入---insert
    删除---delete
    修改---update
    退出---exit
===================
'''
while True:
    print(info,end="")
    try:
        cmd = input("请输入命令：").strip()
        if cmd =="exit":
            break
        func_dict[cmd]()
    except:
        print("输入命令错误！")

