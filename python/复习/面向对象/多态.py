#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print("say hello")

class Pig(Animal):
    def talk(self):
        print("哼哼哼")

class Dog(Animal):
    def talk(self):
        print("汪汪汪")

dog=Dog()
pig=Pig()
p1=People()

def talk(obj):
    obj.talk()

talk(dog)
talk(pig)
talk(p1)