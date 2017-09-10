#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 7:54
# @Author  : Aries
# @Site    : 
# @File    : 可变长函数.py
# @Software: PyCharm

# while True:
#     username = input("请输入用户名")
#     password = input("请输入密码")
#     if username=="admin" and password=="admin":
#         while True:
#             cmd = input("请输入执行命令:")
#             print("====",cmd,"========")
#             if cmd=="exit":
#                 break
#         break
#     else:
#         print("您输入的帐号或密码错误，请重新输入")

# for i in range(1,10):
#     for j in range(1,i):
#         print(i,"*",j,"=",(i*j),end="   ")
#     print("\n")

# while True:
#     name = input("name:")
#     age = input("age:")
#     sex = input("sex:")
#     msg='''
#     =======%s的信息是========
#     名字是%s,年龄是%s,性别是%s
#     =========================
#     ''' %(name,name,age,sex)
#     print(msg)

# msg_dic={'apple':10,'tesla':10000,'mac':3000,'lenovo':33000}
# goods_l=[]
# while True:
#     for key,item in msg_dic.items():
#         print('name:{name} price:{price}'.format(price=item,name=key))
#     choice = input("请输入商品名称:").strip()
#     if choice not in msg_dic:continue
#     count = input("请输入购买个数:").strip()
#     if not count.isdigit():continue
#     goods_l.append((choice,msg_dic[choice],count))
#     print(goods_l)
# # print(msg_dic['apple'])
# name='egon\thello'
# print(name.expandtabs(16))