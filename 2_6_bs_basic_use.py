# -*- coding = utf-8 -*-
# @Time : 2022/1/27 11:43 PM
# @Author : Jieying Dong (Jessie)
# @File : 2_6_bs_basic_use.py
# @Software: PyCharm

# install bs4
# pip install bs4

# 1. get main page source codes and then get child links-href
# 2. enter child links and find the picture links
# 3. download pictures

import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umeitu.com/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find("div", class_="TypeList").find_all("a")
for a in a_list:
    # print(a["href"])
    href = a.get("href")    # get("attribute"): get attributes
    # get child webpage source codes
    nhref = "https://www.umeitu.com/" + href
    child_page_resp = requests.get(nhref)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # get download link from child webpage source codes
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("p", align="center")
    img = p.find("img")
    src = img.get("src")
    # download images
    img_resp = requests.get(src)
    img_name = src.split("/")[-1]    # get contents after last / in url
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)   # img_resp.content: get bytes
    print("over!", img_name)
    time.sleep(1)
print("all over")
