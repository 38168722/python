#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/6 21:40
# @Author  : Aries
# @Site    : 
# @File    : ceshi.py
# @Software: PyCharm
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# mcase = {'a': 10, 'b': 34}
# mcase_frequency={mcase[k]:k for k in mcase}
# print(mcase_frequency)
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency={mcase[k]:k.lower() for k in mcase}
# print(mcase_frequency)

# squared = {x**2 for x in [1,-1,21]}
# print(squared)
# print([(x,y) for x in range(0,6) if x%2==0 for y in range(0,6) if y%2!=0])

# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([row[2] for row in M])
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase1={k.lower():mcase.get(k.upper(),0)+mcase.get(k.upper(),0) for k in mcase.keys()}
# print(mcase1)
# mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
# print(mcase_frequency)
from functools import reduce
lst = [11,22,33]
# func2=reduce(lambda a1,a2:a1+a2,lst)
# print(func2)
print(list([lambda a1,a2,a3:a1+a2+a3,lst]))