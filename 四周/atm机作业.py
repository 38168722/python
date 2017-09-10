#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/6 10:13
# @Author  : Aries
# @Site    : 
# @File    : atm机作业.py
# @Software: PyCharm
import time
def auth(func):
    def inner(*args,**kwargs):
        name=input("帐号:")
        password=input("密码:")
        if name=="egon" and password=="123":
            ret=func(*args,**kwargs)
        else:
            print("帐号或密码错误")
        return ret
    return inner

@auth
def home():
    shijian=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    money=5000     #信用卡额度
    logs=[]
    flag=True
    while flag:
        print('''
        欢迎来到信用卡管理中心
        0、充值
        1、查询余额
        2、查询帐单
        3、提现取款
        4、转帐
        5、退出
        ''')
        sel=input("=>>")
        if sel not in "012345":continue
        if sel=="0":
            while True:
                temp=input("请输入您需要充值的金额:").strip()
                if (not temp) or (not temp.isdigit()):continue
                temp=int(temp)
                money+=temp
                print("充值成功")
                logs.append("%s充值金额%s元"%(shijian,temp))
                break
        elif sel=="1":
                print("您的余额为%s元"%(money))
                logs.append("%s查询余额为%s元"%(shijian,money))
        elif sel=="2":
                print("您的帐单:")
                for i in logs:
                    print(i)
                print("余额共%s元"%(money))
        elif sel=="3":
            while True:
                temp=input("请输入你需要提现的金额:").strip()
                if (not temp) or (not temp.isdigit()):continue
                temp=int(temp)
                money=money-temp-(temp*0.05)
                logs.append("%s提现金额%s元手续费%s元"%(shijian,temp,(temp*0.05)))
                print("提现成功,手续费%s元"%(temp*0.05))
                break
        elif sel=="4":
            while True:
                temp=input("请输入你需要转出的金额:").strip()
                if (not temp) or (not temp.isdigit()):continue
                money-=int(temp)
                logs.append("%s转帐金额为%s元"%(shijian,money))
                print("转帐成功!")
                break
        elif sel=="5":
            print("退出系统，欢迎下次光临")
            flag=False

home()
