#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 8:15
# @Author  : Aries
# @Site    : 
# @File    : lianxi1.py
# @Software: PyCharm

# goods=[]
# msg_dic={"apple":30,"mac":300,"applepine":111}
# flag=True
# while True:
#         if(flag):
#             for i in msg_dic:
#                 print("name:",i,"price:",msg_dic[i])
#             name = input("请输入商品名称").strip()
#             if len(name)==0 or name not in msg_dic:continue
#         count = input("请输入要购买的数量")
#         if not count.isdigit():
#             flag=False
#             continue
#         flag=True
#         count=int(count)
#         goods.append((name,msg_dic[name],count))
#         print(goods)

# s = "hello alex alex say sb sb"
# dic={}
# for i in s.split():
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)
# 　　pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# 　　linuxs={'wupeiqi','oldboy','gangdan'}
# 　　1. 求出即报名python又报名linux课程的学员名字集合
# 　　2. 求出所有报名的学生名字集合
# 　　3. 求出只报名python课程的学员名字
# 　　4. 求出没有同时这两门课程的学员名字集合

# pylinux=[]
# for i in pythons:
#     if i in linuxs:
#         pylinux.append(i)
# print(pylinux)
# for i in linuxs:
#     if i not in pythons:
#         pythons.append(i)
#
# print(pythons)
# onlypython=[]
# for i in pythons:
#     if i not in linuxs:
#         onlypython.append(i)
# print(onlypython)

# pythons={'jack','mary','frank','cat','gangdan','biubiu'}
# linuxs={'cat','tom','frank'}
# # print(pythons&linuxs)
# # print(pythons.intersection(linuxs))
# # print(pythons-linuxs)
# # print(pythons.difference(linuxs))
# print(pythons.symmetric_difference(linuxs))
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
def test1():
    print("hello world")