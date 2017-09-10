#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 13:31
# @Author  : Aries
# @Site    : 
# @File    : day9.py
# @Software: PyCharm
#1、9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",(i*j),end="  ")
#     print()
# 2、简单购物车
# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
# goods=[]
# while True:
#     print("=====商品信息如下所示=====")
#     for k,v in msg_dic.items():
#         print("商品名称:",k," 价格:",v)
#     name = input("请输入要购买的商品名称")
#     if name not in msg_dic.keys():
#         print("商品名称有误，请重新输入")
#         continue
#     num = int(input("请输入商品数量"))
#     goods.append((name,msg_dic[name],num,(int(msg_dic[name])*num)))
#     print(goods)
# 3 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# jihe={11,22,33,44,55,66,77,88,99,90}
# k1=[]
# k2=[]
# for i in jihe:
#     if i>=66:
#         k1.append(i)
#     else:
#         k2.append(i)
# print("k1===",k1)
# print("k2===",k2)
 #2 统计s='hello alex alex say hello sb sb'中每个单词的个数
# s1="hello alex alex say hello sb sb"
# num=set()
# for i in s1.split(" "):
#     num.add((i,s1.count(i)))
# print(num)

#求字母出现个数
# dict2 = {}
# s='hello alex alex say hello sb sb'
# list1 = s.split()
# print(list1)
# for i in range(len(list1)):
#     count = 0
#     for j in range(len(list1)):
#         if list1[i] == list1[j]:
#             count += 1
#             dict2[list1[i]] = count
# print(dict2)

import time

def add():
    print("添加功能")

def delete():
    print("删除功能")

def change():
    print("更改功能")

def select():
    print("查看功能")

def update():
    print("更新功能")

func_dir={
    'select':select,
    'delete':delete,
    'change':change,
    'add':add
}

#
# while True:
#   cmd = input(">>:").strip()
#   if not cmd:continue
#   if cmd in func_dir:
#       func_dir[cmd]()
#   else:
#       print("无效的命令")
#

