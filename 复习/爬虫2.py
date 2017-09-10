#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 19:13
# @Author  : Aries
# @Site    : 
# @File    : 爬虫2.py
# @Software: PyCharm
# from urllib.request import urlopen
# import re
# def get_page(url):
#     return urlopen(url).read().decode("utf-8")
#
# page=get_page("http://m.maoyan.com/")
# ret=re.findall("","rabhdg8sd")
# print(ret)

# data={"time ":"2016-08-05T13:13:05 ","some_id ":"I D1234 ","fld7":7,
#      "grp1":{"fld1":1,"fld2":2},"xxx2":{"fld3":0,"fld5":0.4},
#      "fld6":11,"fld7":7,"fld46":8}
# fields="fld2|fld3|fld7|fld19"
# # print(fields_list)
# def select(data,filed,result={}):
#     field_l=filed.split("|")
#     for key in data:
#         if key in field_l:
#             result[key]=data[key]
#         if type(data[key]) is dict:
#             select(data[key],filed)
#     return result
# print(select(data,fields))

# data={"time ":"2016-08-05T13:13:05 ","some_id ":"I D1234 ","fld7":7,
#      "grp1":{"fld1":1,"fld2":2},"xxx2":{"fld3":0,"fld5":0.4},
#      "fld6":11,"fld7":7,"fld46":8}
# fields="fld2|fld3|fld7|fld19"
# def select(data,fields,result={}):
#     fields_list = fields.split('|')
#     for key in data:
#         if key in fields_list:
#             result[key] = data[key]
#         if type(data[key]) is dict:
#             select(data[key],fields)
#     # print(result)
#     return result    #返回结果
# print(select(data,fields))


def sum(int array[],int size):
    k=0
    s=0
    while k<size:
        s=s+array[k]
        k=k+1

