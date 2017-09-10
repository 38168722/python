#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 16:41
# @Author  : Aries
# @Site    : 
# @File    : 函数.py
# @Software: PyCharm
# 1、整理函数相关知识点，画思维导图
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def cal_count(name):
#     num_count=0
#     letter_count=0
#     space_count=0
#     other_count=0
#     for i in name:
#         if i.isdigit():
#             num_count+=1
#         elif i.isalpha():
#             letter_count+=1
#         elif i.isspace():
#             space_count+=1
#         else:
#             other_count+=1
#     return {"数字数":num_count,"字符数":letter_count,"空格数":space_count,"其它数":other_count}
# print(cal_count("kkkk"))

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def mylen(name):
#     if len(name)>5:
#         return "长度大于5"
#     return "长度小于5"
#
# print(mylen([1,2,3,4]))
# print(mylen("1,2,3,4,5"))

# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def mylen(name):
#     if len(name)>2:
#         return name[0:2]
#     return name
# print(mylen(["hello","abcd","wogan"]))

# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def mylen(name):
#     abc=[]
#     for i in range(len(name)):
#         if i%2!=0:
#             abc.append(name[i])
#     return abc
# print(mylen(["222","333","444","555"]))
# from urllib.request import urlopen
# def getUrl(url):
#     def inner():
#         abc=urlopen(url).read()
#         return abc
#     return inner
#
# abc=getUrl("http://www.baidu.com")
# print(abc())
# import pickle
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
# output = open('data.pkl','w',encoding="utf-8")
# pickle.dump(data1, output)
# pickle.dump(selfref_list, output, -1)
# output.close()

s1="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
print(s1.replace(" ",""))