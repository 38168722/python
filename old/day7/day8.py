#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 8:20
# @Author  : Aries
# @Site    : 
# @File    : day8.py
# @Software: PyCharm

tag = True
while tag:
    user = input('====》user:').strip()
    password = input('====》password:').strip()
    salary = input('====》salary:').strip()
    work_mons = input('====》work_mons:').strip()
    if len(user) != 0 and len(password) != 0 and salary.isdigit() == True and work_mons.isdigit() == True:
        userinfo = '''
            user: %s
            password: %s
            work_mons: %s
            salary: %s
            '''%(user,password,work_mons,salary)
        print(userinfo,end='')

        while tag:
            print('''
                1 查询总工资
                2 查询用户身份
                3 退出登录
            ''')
            s = int(input('====》请输入按键：').strip())
            if s == 1:
                print( int(work_mons)*int(salary))
            if s == 2:
                if user == 'alex':
                    print('super user')
                elif user in ['yuanhao','wupeiqi','egon']:
                    print('normal user')
                else:
                    print('unkown user')
            if s == 3:
                tag = False