#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 15:54
# @Author  : Aries
# @Site    : 
# @File    : day7默写.py
# @Software: PyCharm
while True:
    name = input("please input your name ")
    password = input("please input your password ")
    if name=='egon' and password=='123':
        print("login successfull")
        while True:
            cmd = input(">>:")
            if cmd=="quit":
                break
            print("====>",cmd)
    else:
        print("您输入的用户或密码有误，请重新输入.")
        continue
    break

# flag = True
# while flag:
#     username = input("请输入用户名")
#     password = input("请输入密码")
#     if username=="egon" and password=="123":
#         print("login successfull!")
#         while flag:
#             cmd = input("=>")
#             if cmd=="quit":
#                 flag=False
#             else:
#                 print(cmd)
#     else:
#         print("您输入的帐号或密码错误,请重新输入")

# count=0
# while count<10:
#     if count==3:
#         count+=1
#         continue
#     print(count)
#     count+=1
# else:
#     print("最后执行，并且只有在while循环没有被break的情况下才执行。")

#移除空白
# while True:
#     name=input("user: ").strip()
#     password=input('password: ').strip()
#     if name=='egon' and password =='123':
#         print("login successfull")

# while True:
#     cmd = input('>>: ').strip()
#     if len(cmd)==0:continue
#     cmd_l = cmd.split()
#     print('命令是:%s 命令的参数是:%s' %(cmd_l[0],cmd_l[1]))

# while True:
#     age = input(">>: ").strip()
#     if len(age)==0:continue
#     if age.isdigit():
#         age=int(age)
#     else:
#         print('must be int')

# print('my name is {} my sex is {} my age is {}'.format('egon','male',18))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end="  ")
#     print(" ")
#
# dict = {"name":"egon","sex":"male","age":"33"}
# for k,v in dict.items():
#     print(k,"===",v)
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack.pop())

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
