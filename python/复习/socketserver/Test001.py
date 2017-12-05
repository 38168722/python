#!/usr/bin/env python
# -*- coding: utf-8 -*-

URLpattern=(("/login","login"),("/auth","auth"))
for item in URLpattern:
    print(item[0])
    print(item[1])