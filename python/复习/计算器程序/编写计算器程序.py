#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/5 14:02
# @Author  : Aries
# @Site    : 
# @File    : 编写计算器程序.py
# @Software: PyCharm
import re



bracket = re.compile(r'\([^()]+\)')  # 寻找最内层括号规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')  # 寻找乘法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')  # 寻找除法运算规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻找加法运算规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')  # 寻找减法运算规则
c_f = re.compile(r'\(?\+?-?\d+\)?')  # 检查括号内是否运算完毕规则
strip = re.compile(r'[^(].*[^)]')  # 脱括号规则
chengshi="1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"





