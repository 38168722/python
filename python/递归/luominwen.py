#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 15:06
# @Author  : Aries
# @Site    : 
# @File    : luominwen.py
# @Software: PyCharm
import re
s="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# s="1000-100-400+(200+(200-50)*2)-2000/4+(200+(100-200)*2)"
# s="(3/4+1/2)/5/8+(60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))+(200+(100-200)*2)"
# s="1+2+3+4+5+6+7+8+9+11+22+33+44+55+6+6+77+88+99+123+12+123+32+32+32+12+235+76+34+27+72+27+2+27+7+7+2+3+1+8+0+1"
s=s.replace(" ","")
print(s)

def multi(s):
    s=s.split("*")
    multi_sum = float(s[0]) * float(s[1])
    return str(multi_sum)
def division(s):
    s=s.split("/")
    divis_sum=float(s[0])/float(s[1])
    return str(divis_sum)
def cut(s):
    s = change(s)
    if "*" in s or "/" in s:
        a =re.search(r"\d+\.?\d*[*/]\-?\d+\.?\d*",s).group()
        if "*" in a:
            s_replace = multi(a)
        elif "/" in a:
            s_replace = division(a)
        s=s.replace(a,s_replace)
        return cut(s)
    else:
        return add(s)
def Addition_subtraction(s):
    if "+" in s:
        s=s.split("+")
        t_sum=float(s[0]) + float(s[1])
    else:
        s = s.rsplit("-",1)
        print(s)
        t_sum = float(s[0])-float(s[1])
    return str(t_sum)
def add(s):
    s = change(s)
    print("add_s=%s"%s)
    k=s.split("-")
    if "+" not in s and "-" not in s:
        return s
    elif "+" not in s and len(k)==2 and k[0] =="":
        return s
    else:
        a = re.search(r"\-?\d+\.?\d*[+-]\d+\.?\d*", s).group()
        s_replace = Addition_subtraction(a)
        s = s.replace(a, s_replace,1)
        return add(s)

def find(s):
    if "(" in s and ")" in s:
        a =re.search(r"\([^(]*?\)",s).group()
        b=re.split(r"[()]",a)
        s_replace=cut(b[1])
        s =s.replace(a,s_replace,1)
        s = change(s)
        return find(s)
    else:
        return cut(s)
def change(s):
    s =s.replace("++","+")
    s =s.replace("+-","-")
    s =s.replace("-+","-")
    s =s.replace("--","+")
    return s
print("find(s)=",find(s))
print("eval(s)=",eval(s))
