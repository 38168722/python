#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 17:05
# @Author  : Aries
# @Site    :
# @File    : aa.py
# @Software: PyCharm
# import os
# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
# goods_l=[]
# while True:
#     for key,item in msg_dic.items():
#         print('name:{name} price:{price}'.format(price=item,name=key))
#     choice=input('商品>>: ').strip()
#     if not choice or choice not in msg_dic:continue
#     count=input('购买个数>>: ').strip()
#     if not count.isdigit():continue
#     goods_l.append((choice,msg_dic[choice],count))
#      print(goods_l)

# c=[11,22,33,44,55,66,77,88,99,90]
# a={'k1':[],'k2':[]}
# for i in c:
#     if i>66:
#         a['k1'].append(i)
#     elif i<66:
#         a['k2'].append(i)
# print(a)

# for i in range(11):
#     if i in [4,5,6]:
#         continue
#     print(i)

# count=0
# while count < 10:
#     if count<=5 or count>=7:
#         print(count)
#     count+=1
for i in range(1,11):
    print(i,end=" ")