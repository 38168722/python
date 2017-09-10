#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 8:35
# @Author  : Aries
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
# count=0
# while count<10:
#     if count==5:
#         break
#     print(count)
#     count+=1
#
# count=0
# while count<10:
#     count+=1
#     if count in [4,5,6]:
#         continue
#
#     print(count)

# while True:
#     age = int(input("请输入老男孩的年龄:"))
#     if(age>56):
#         print("您输入的年龄太大了")
#     elif(age<56):
#         print("您输入的年龄太小了")
#     else:
#         print("您猜对了!")
#         break

while True:
    score = input(">>:")
    score = int(score)
    if score>=90:
        print('A')
    if score>=80:
        print('B')
    if score>=70:
        print('C')
    if score>=60:
        print('D')
    if score<60:
        print('E')