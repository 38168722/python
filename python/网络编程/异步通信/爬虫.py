#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28 11:15
# @Author  : Aries
# @Site    : 
# @File    : 爬虫.py
# @Software: PyCharm
from multiprocessing import Pool
import requests
import os
def get_page(url):
    print("<%s> get <%s>"%(os.getpid(),url))
    response=requests.get(url)
    return {"url":url,"text":response.text}

def parse_page(res):
    print("<%s> parse [%s]"%(os.getpid(),res["url"]))
    with open("db.txt",'a') as f:
        parse_res="url:%s size:%s\n" %(res["url"],len(res["text"]))
        f.write(parse_res)

if __name__ == '__main__':
    p=Pool(4)
    urls=[
        'https://www.baidu.com',
        'http://www.openstack.com',
        'https://www.python.com',
        'http://www.sina.com.cn'
    ]
    # obj_l=[]
    # for url in urls:
    #     obj=p.apply_async(get_page,args=(url,))
    #     obj_l.append(obj)
    # p.close()
    # p.join()
    # print([obj.get() for obj in obj_l])
    for url in urls:
        p.apply_async(get_page,args=(url,),callback=parse_page)
    p.close()
    p.join()
    print("主",os.getpid())