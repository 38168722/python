#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
v=subprocess.getoutput("ipconfig")
value=v[20:30]
print(value)