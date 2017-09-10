#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/19 8:49
# @Author  : Aries
# @Site    : 
# @File    : 计算器.py
# @Software: PyCharm
import re
s1="1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
clear_brackets=re.compile("\([^()]+\)")
chenchu=re.compile("\d+\.?\d*[*/]-?\d+\.?\d*")#"\d+\.?\d*[*/]\.?\d+\.?\d*"
jiajian=re.compile("\d+\.?\d*[-\+]-?\d+\.?\d*")#-?[1-9]\d*\.\d*|-0\.\d*[1-9]\d*

def writefile(strname):
    with open("chengxu.log","a") as wr:
        wr.write(str(strname)+'\n')


def operation(suanshu):
    while True:
        try:
            yunsuan=chenchu.search(suanshu).group()
        except Exception:
            # writefile('cc'+yunsuan)
            break
        if "*" in yunsuan:
            num1,num2=re.split("\*",yunsuan)
            result=float(num1)*float(num2)
            suanshu=suanshu.replace(str(yunsuan),str(result))
            print('++++++++++++++++',suanshu)
            # suanshu=suanshu.replace(result,yunsuan)
            operation(clear_k(s1))
        if "/" in yunsuan:
            num1,num2=re.split("\/",yunsuan)
            result=float(num1)/float(num2)
            suanshu=str(suanshu)
            suanshu=suanshu.replace(yunsuan,str(result))
    while True:
        try:
            yunsuan=jiajian.search(suanshu).group()
            if("--" in yunsuan):
                yunsuan=yunsuan.replace("--","+")
            elif("-+" in yunsuan):
                yunsuan=yunsuan.replace("-+","-")
            elif("+-" in yunsuan):
                yunsuan=yunsuan.replace("+-","-")
        except Exception:
            # writefile('++'+yunsuan)
            break
        if "+" in yunsuan:
            num1,num2=re.split("\+",yunsuan)
            result=float(num1)+float(num2)
            suanshu=suanshu.replace(str(yunsuan),str(result))
        if "-" in yunsuan:
            num1,num2=re.split("\-",yunsuan)
            result=float(num1)-float(num2)
            suanshu=suanshu.replace(str(yunsuan),str(result))
    # writefile('sss'+suanshu)
    return suanshu

def clear_k(str2):
    try:
        s1=clear_brackets.search(str2).group()
    except AttributeError:
        return str2,str2
    s2=s1.strip("()").strip()
    # if s1==s2:
    return s1,s2


#s1="1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
flag=True
s2=None
while flag:

   s1=s1.replace(clear_k(s1)[0],str(operation(clear_k(s1)[1])))
   writefile('ssssssss'+s1)
   if s2==s1:
       s1=operation(s1)
       break
   with open('iiii','w')as lll:
       lll.write(str(s1)+'\n')
   print(s1)
   s2=s1


print(s1)


# s2=clear_brackets.search(s1).group()
# abc=s2.strip("()")
# a,b=abc.split("/")
# h=int(a)/int(b)
# s1=s1.replace(s2,str(h))
# hdf=clear_brackets.search(s1)
# hdf=hdf.group().strip("()")
# while True:
#     try:
#         x1=operater.search(hdf).group()
#     except AttributeError:
#         break
#     if "*" in x1:
#         num1,num2=re.split("\*",x1)
#         result=float(num1)*float(num2)
#         hdf=hdf.replace(x1,str(result))
#     elif "/" in x1:
#         num1,num2=re.split("\/",x1)
#         result=float(num1)/float(num2)
#         hdf=hdf.replace(x1,str(result))
# print("hdf",hdf)
# while True:
#     try:
#         x1=jiajian.search(hdf).group()
#     except AttributeError:
#         break
#     if "+" in x1:
#         num1,num2=re.split("\+",x1)
#         result=float(num1)+float(num2)
#         hdf=hdf.replace(x1,str(result))
#     elif "-" in x1:
#         num1,num2=re.split("\-",x1)
#         result=float(num1)-float(num2)
#         hdf=hdf.replace(x1,str(result))
# print("s1",s1)
# s1.replace()
# print("加减算完的hdf",hdf)
import socketserver