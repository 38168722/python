#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 17:25
# @Author  : Aries
# @Site    : 
# @File    : 员工信息管理.py
# @Software: PyCharm
import os
# select name,age where age > 22
# select * where dept = "IT"
# select * where phone like "136"
def query(data):
    data1 = data.split(" ")
    if data ==("select name,age where age > %s"%(data1[5])):
        with open("xinxi","r", encoding="utf-8") as f:
            list = []
            for line in f:
                i = line.strip().split(",")
                if i[2] > data1[5]:
                    list.append(i[0:3])
                    # print(i)
            for k in list:
                print(k)
            print("查询到 %s 条符合的信息" % len(list))
    elif data ==("select name,age where age < %s"%(data1[5])):
        with open("xinxi","r", encoding="utf-8") as f:
            list = []
            for line in f:
                i = line.strip().split(",")
                if i[2] < data1[5]:
                    list.append(i[0:3])
                    # print(i)
            for k in list:
                print(k)
            print("查询到 %s 条符合的信息" % len(list))
    elif data ==("select * where age > %s"%(data1[5])):
        with open("xinxi","r", encoding="utf-8") as f:
            list = []
            for line in f:
                i = line.strip().split(",")
                if i[2] > data1[5]:
                    list.append(i)
                    # print(i)
            for k in list:
                print(k)
            print("查询到 %s 条符合的信息" % len(list))
    elif data == ("select * where dept = %s" % (data1[5])):
            with open("xinxi","r", encoding="utf-8") as f:
                list1 = []
                for line in f:
                    i1 = line.strip().split(",")
                    if i1[4] == data1[5]:
                        list1.append(i1)
                for j in list1:
                    print(j)
                print("查询到 %s 条符合的信息" % len(list1))
    else:
        if data == ("select * where phone like %s" % (data1[5])):
            with open("xinxi","r", encoding="utf-8") as f:
                list = []
                for line in f:
                    i = line.strip().split(",")
                    if data1[5] in i[3]:
                        list.append(i)
                for k in list:
                    print(k)
                print("查询到 %s 条符合的信息" % len(list))
    return 0

#name,age,phone,dept
def add(data):
    data1=data.split(",")
    with open ("xinxi","r",encoding="utf-8") as f:
        list=[]
        phone_list=[]
        for line in f:
            i=line.strip().split(",")
            phone_list.append(i[3])
        if data1[2] in phone_list:
            print("手机号码已存在！")
        else:
            with open ("xinxi","r+",encoding="utf-8") as f1:
                for line in f1:
                    i1=line.strip().split(",")
                    list.append(i1)
                w=str(int(list[-1][0])+1)
                data1.insert(0,w)
                print(data1)
                data1=",".join(data1)
                f1.write("\n")
                print("data1=====",data1)
                f1.write(data1)
                f1.flush()
                print("添加成功！")
    return 0

#delete from staff_table where staff_id = 12
def delete(data):
    data1=data.split(" ")
    print(data1)
    if data==("delete * where id = %s"%(data1[5])):
        with open("xinxi","r",encoding="utf-8") as f:
            list=[]
            for line in f:
                i =line.strip().split(",")
                i1=line.splitlines()
                if data1[5]==i[0]:
                    i2=",".join(i1)
                    print(i2)
                    list.append(i)
        a=i2
        f=open ("xinxi","r",encoding="utf-8")
        f1=open ("xinxi_new","a+",encoding="utf-8")
        for i in f:
            if a in i:
                i=i.replace(a,"").strip()
            f1.write(i)
            f1.flush()
        f.close()
        f1.close()
    os.remove("xinxi")
    os.rename("xinxi_new","xinxi")
    print("删除成功")
    return 0

#UPDATE SET dept = IT where dept = 运维
def change(data):
    data1=data.split(" ")
    with open("xinxi","r",encoding="utf-8") as f,open("xinxi2","w",encoding="utf-8") as f1:
        for line in f:
            i = line.strip()
            print(i)
            if data1[8] in i:
                i = i.replace(data1[8],data1[4])
            f1.write(i)
            f1.write("\n")
            f1.flush()
    os.remove("xinxi")
    os.rename("xinxi2","xinxi")
    print("修改成功")
    return 0


#主程序
while True:
    print('''
            ============================
                欢迎来到员工信息系统
            ----------------------------
                    1.查询
                    2.添加
                    3.修改
                    4.删除
                    5.退出
            ===========================
    ''')
    choice=input("请输入序号：")
    if choice=="1":
        print("\t\t\t=====================语法实例=====================")
        print("""
            select name,age where age > 22
            select * where dept = IT
            select * where phone like 133
        """)
        data = input("请输入语法>>:").strip()
        query(data)

    if choice =="2":
        print("\t\t\t=====================语法实例=====================")
        print("""
              name,age,phone,dept
              注意:内容添加后xixin文件不会马上有变化要把程序停了重新运行才能看到效果，这个是内存写入有延迟造成的,即便我用了flush方法它还是没即时写到文件中。

              """)
        data = input("请输入语法>>:").strip()
        add(data)

    if choice=="3":
        print("\t\t\t=====================语法实例=====================")
        print("""
            update set dept = IT where dept = 运维
            注意:内容修改后文件不会马上有变化要做程序停了重新运行才能看到效果，这个是内存写入有延迟造成的,即便我用了flush方法它还是没即时写到文件中。
            """)
        data = input("请输入语法>>:").strip()
        change(data)

    if choice=="4":
        print("\t\t\t=====================语法实例=====================")
        print("""
            delete * where id = 12
            注意:内容删除后文件不会马上有变化要做程序停了重新运行才能看到效果，这个是内存写入有延迟造成的,即便我用了flush方法它还是没即时写到文件中。

            """)
        data = input("请输入语法>>:").strip()
        delete(data)
    if choice=="5":
        break