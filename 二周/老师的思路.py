#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/5 7:52
# @Author  : Aries
# @Site    : 
# @File    : 老师的思路.py
# @Software: PyCharm
import os
column_d = {'id':0,'name':1,'age':2,'phone':3,'job':4}
def getColumn(content):
    column=content.lstrip('select ')
    return column.strip().split(',')

def condition_handler(fileName,condition):
    data=[]
    if ">" in condition:
        condition=condition.split(">")
        with open(fileName,encoding="utf-8") as fr:
            for line in fr:
                line=line.strip().split(",")
                line[column_d[condition[0]]]
                if int(line[column_d[condition[0]]])>int(condition[1]):
                        data.append(line)
    if "<" in condition:
        condition=condition.split("<")
        with open(fileName,encoding="utf-8") as fr:
            for line in fr:
                line=line.strip().split(",")
                line[column_d[condition[0]]]
                if int(line[column_d[condition[0]]])<int(condition[1]):
                        data.append(line)
    if "=" in condition:
        condition=condition.split("=")
        with open(fileName,encoding="utf-8") as fr:
            for line in fr:
                line=line.strip().split(",")
                line[column_d[condition[0]]]
                if int(line[column_d[condition[0]]])==int(condition[1]):
                        data.append(line)
    if "like" in condition:
        condition=condition.strip().split(" like ")
        with open(fileName,encoding="utf-8") as fr:
            for line in fr:
                line=line.strip().split(",")
                if condition[1] in line[column_d[condition[0]]]:
                        data.append(line)
    return data

def display():
    s=input("=>>").strip()
    content,condition=s.split(" where ")
    column_l = getColumn(content)
    content_l=condition_handler("xinxi",condition)
    for i in content_l:
        for line in column_l:
            if "*" in column_l:
                print(i,end=" ")
            else:
                print(i[column_d[line]],end=" ")
        print("")

def add():
    import os
    user=input("=>>")
    data=[]
    with open("xinxi",encoding="utf-8") as fr:
        for line in fr:
            data.append(line.strip())
    with open("xinxi.bak","w+",encoding="utf-8") as wr:
        for i in data:
            wr.write(i+"\n")
        wr.write((str(int(data[len(data)-1][0])+1))+","+user+"\n")
        fr.close()
        wr.close()
        os.remove("xinxi")
        os.rename("xinxi.bak","xinxi")
        print("添加成功")

def delete(id):
    with open("xinxi",encoding="utf-8") as fr:
        with open("xinxi.bak","w+",encoding="utf-8") as wr:
            for f in fr:
                content=f.split(",")
                if id==f[0]:
                    continue
                wr.write(f)
    os.remove("xinxi")
    os.rename("xinxi.bak","xinxi")
    print("删除成功!")

def update(oldstr,newstr):
    with open("xinxi",encoding="utf-8") as fr:
        with open("xinxi.bak","w+",encoding="utf-8") as wr:
            for i in fr:
                wr.write(i.replace(oldstr,newstr))
        wr.close()
        fr.close()
        os.remove("xinxi")
        os.rename("xinxi.bak","xinxi")
        print("更新成功")

# while True:
#     display()
# delete("2")

update("运维","IT")