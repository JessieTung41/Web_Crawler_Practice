# -*- coding = utf-8 -*-
# @Time : 2022/1/30 4:15 PM
# @Author : Jieying Dong (Jessie)
# @File : 4_5_pool_case.py
# @Software: PyCharm

# 1. How to get the content in single page
# 2. Use thread pool and Get many pages together

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_page(url):
    resp = requests.get(url, headers={
        "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    })
    html = etree.HTML(resp.text)
    li = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li")
    for l in li:
        lst = []
        cname = l.xpath("./div/div[2]/div[1]/a/span[1]/text()")[0]
        lst.append(cname)
        ename = l.xpath("./div/div[2]/div[1]/a/span[2]/text()")[0].replace("/", " ").strip()
        lst.append(ename)
        info1 = l.xpath("./div/div[2]/div[2]/p[1]/text()")[0].strip()
        info2 = l.xpath("./div/div[2]/div[2]/p[1]/text()")[1].strip()
        lst.append(info1)
        lst.append(info2)
        score = l.xpath("./div/div[2]/div[2]/div/span[2]/text()")[0]
        lst.append(score)
        people = l.xpath("./div/div[2]/div[2]/div/span[4]/text()")[0]
        lst.append(people)
        des = l.xpath("./div/div[2]/div[2]/p[2]/span/text()")
        if len(des) != 0:
            des = des[0].replace("。", "")
            lst.append(des)
        else:
            lst.append(" ")
        csvwriter.writerow(lst)
    print(url, "finish!!!")

    # print(resp.text)

if __name__ == "__main__":
    # for i in range(10):
    #     download_one_page(f"https://movie.douban.com/top250?start={str(i*25)}")

    with ThreadPoolExecutor(6) as t:
        for i in range(0,10):
            istr = str(i*25)
            t.submit(download_one_page, f"https://movie.douban.com/top250?start={istr}")
    print("over!!!")
    # for i in range(10):
    #     download_one_page(f"https://movie.douban.com/top250={str(9*25)}")
