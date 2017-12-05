#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app01 import views
URLpattern=(
    ("/login",views.login),
    ("/auth",views.auth),
    ("/reg",views.reg),
    ("/zhuce",views.zhuce)
)