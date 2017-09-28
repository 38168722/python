#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 17:13
# @Author  : Aries
# @Site    : 
# @File    : 抽象类.py
# @Software: PyCharm
from abc import ABCMeta,abstractmethod
class E:
    def test(self):
        print("from E")


class A(E):pass
    # def test(self):
    #     print("from A")
class B(E):
    def test(self):
        print("from B")
class C(E):
    def test(self):
        print("from C")
class D(A,B,C):
    # def test(self):
    #     print("from D")
    pass

d=D()
d.test()
print(D.mro())