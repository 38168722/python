#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# response=requests.get("http://www.autohome.com.cn/news/")
# response.encoding="gbk"
#
# with open("autohome_new_txt","w",encoding="utf-8") as f:
#     f.write(response.text);


with open("autohome_new_txt","r",encoding="utf-8") as f:
    data=f.read()
soup=BeautifulSoup(data,"html.parser")
tag=soup.find(name="div",attrs={'id':'auto-channel-lazyload-article'})
li_list=tag.find_all("li")
for li in li_list:
    h3=li.find(name="h3")
    if not h3:
        continue
    print(h3.text)
    print(li.find(name="a").get("href"))
    print(li.find(name="a").attrs["href"])
