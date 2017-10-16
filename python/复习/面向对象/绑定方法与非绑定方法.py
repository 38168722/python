#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import pickle
class People:
    def __init__(self,name,sex,user_id):
        self.name=name
        self.sex=sex
        self.user_id=user_id

    def bar(self):
        print("---->",self.name)

    def create_id(self):
        m=hashlib.md5()
        m.update(self.name.encode("utf-8"))
        m.update(self.sex.encode("utf-8"))
        m.update(str(self.user_id).encode("utf-8"))
        return m.hexdigest()

    def save(self):
        with open(self.id,"wb") as f:
            pickle.dump(self,f)


class Teacher:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

    # def __del__(self):
    #     print("###############")

    def __getitem__(self, item):
        return getattr(self,item);

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def __delitem__(self, key):
        delattr(self,key)

t1=Teacher("egon")
print(t1["name"])