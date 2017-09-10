#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/9 19:05
# @Author  : Aries
# @Site    : 
# @File    : Test1.py
# @Software: PyCharm
# print([i for i in range(100)])
# def foo():
#     # print("starting")
#     while True:
#         x=yield
#         print("value: ",x)
# g=foo()
# g.send(None)
# g.send(10)
# next(g)
# # g.send(20)

# def warrap(func):
#     def inner(*args,**kwargs):
#         ret = func()
#         next(ret)
#         return ret
#     return inner
#
# @warrap
# def foo():
#     print("starting....")
#     while True:
#         x=yield
#         print("value:",x)
#
# g=foo()
# g.send(10)
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
@init
def eater(name):
    print("%s read to eat" %name)
    food_list=[]
    while True:
        food=yield food_list
        food_list.append(food)
        print("%s start to eat %s"%(name,food))

# e=eater('alex')
# print(e.send("狗屎"))
# print(e.send("猫屎") )
# def demo1(*args,*kwargs):
#     print(args)
#     print(kwargs)
#
# demo1(123,a=10)

# def Person(*args,**kwargs):
#     self=[]
#     def __init__(name,life_value,aggr):
#         self['name']=name
#         self['life_value']=life_value
#         self['aggr']=aggr
#         return self
#

class Person:
    money=10000
    role="中国人"
    def __init__(self,name,life_value,aggr):
        self.name=name
        self.life_value=life_value
        self.aggr=aggr


    def attack(self,obj):
        obj.life_value=obj.life_value-self.aggr


egon=Person('egon',100000,100)
alex=Person('alex',100000,25)
# egon.attack(alex)




class Dog:
    def __init__(self,name,life_value,aggr):
        self.name=name
        self.life_value=life_value
        self.aggr=aggr

    def attack(self,obj):
        obj.life_value-=self.aggr


class Weapon:
    def __init__(self,name,aggr,life_value,price,attack_force):
        self.price=price
        self.name=name
        self.aggr=aggr
        self.life_value=life_value
        self.attack_fore=attack_force
    def update(self,person):
        person.money=person.money-self.price
        person.aggr=person.aggr+self.aggr
        person.life_value=person.life_value+self.life_value
    def kill(self,obj):
        obj.life_value=obj.life_value-self.attack_fore



wangcai=Dog("汪汪",1000,500)
alex=Person("alex",10000,100)
print(alex.Weapon.kill(wangcai))
