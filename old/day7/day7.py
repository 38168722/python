#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 14:14
# @Author  : Aries
# @Site    : 
# @File    : day7.py
# @Software: PyCharm
#1：编写for循环，利用索引遍历出每一个字符（选做题）
# msg='hello egon 666'
# for i in range(len(msg)):
#     print(msg[i])

#2：编写while循环，利用索引遍历出每一个字符
# msg='hello egon 666'
# count=0
# while count<len(msg):
#     print(msg[count])
#     count+=1

#3：msg='hello alex'中的alex替换成SB
# msg='hello alex'
# msg=msg.replace('alex','SB')
# print(msg)

#4：将该字符的文件名，文件大小，操作方法切割出来
# msg='/etc/a.txt|365|get'
# msg=msg.split("|")
# print("文件名",msg[0],"文件大小",msg[1])

#5.编写while循环，要求用户输入命令，如果命令为空，则继续输入
# while True:
#     username = input("name:")
#     password = input("password")
#     if len(username)<=0 and len(password)<=0:
#         continue
#     else:
#         while True:
#             cmd = input("==>")
#             print(cmd)
#             if cmd == "quit":
#                 break
#     break

#6、编写while循环，让用户输入用户名和密码，如果用户为空或者数字，则重新输入
# while True:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if len(username)<=0 or str(username).isdigit():
#         print("用户不能为数字请重新输入")
#         continue
#     print("login successful")
#     break
#7、编写while循环，让用户输入内容，判断输入的内容以alex开头的，则将该字符串加上_SB结尾
# while True:
#     content = input("请输入内容:")
#     if (str(content).startswith("alex")):
#         content=content+"_SB"
#     print(content)

#8
flag=True
while flag:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    work_time = input("输入工作了几个月")
    per_salary = input("输入每月的工资")
    if len(username)<=0 or len(password)<=0 or (not work_time.isdigit()) or (not per_salary.isdigit()):
        continue
    else:
        print("user: ",username)
        print("password: ",password)
        print("work_mons: ",work_time)
        print("salary: ",per_salary)
        while flag:
            print('''
            1查询总工资
            2查询用户身份
            3退出登录
            ''')
            cmd = input("=>>")
            if cmd=="1":
                print("总工资是：",(int(per_salary)*int(work_time)))
            elif cmd=="2":
                if username=='alex':
                    print("你的帐号是 super user")
                elif username in ['yuanhao','wupeiqi']:
                    print("你的帐号是 normal user")
                else:
                    print("unkown user")
            elif cmd=="3":
                print("欢迎您的使用，再见")
                flag=False




