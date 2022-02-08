# -*- coding = utf-8 -*-
# @Time : 2022/2/8 5:54 PM
# @Author : Jieying Dong (Jessie)
# @File : 05_KFC.py
# @Software: PyCharm

import requests
import json


url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"

param = {
    "op": "keyword"
}

headers = {
    "User-Agent": "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 97.0.4692.99 Safari / 537.36"
}

lst = []
# fp = open("./KFC.json", mode="a", encoding="utf-8")
# fp.write("{")

location = input("Put the location: ")

for i in range(1, 20):
        data = {
                "cname": "",
                "pid": "",
                "keyword": location,
                "pageIndex": str(i),
                "pageSize": "10"
        }
        # print(data)
        resp = requests.post(url, params=param, data=data, headers=headers)

        tex = resp.text
        # print(tex)

        t = json.loads(tex)
        t = t["Table1"]
        if len(t) == 0:
                break
        lst.append(t)
        # print(t, type(t))
        # fp = open("./KFC.json", mode="a", encoding="utf-8")
        #
        # json.dump(t, fp=fp, ensure_ascii=False)
        # fp.write(",")
        print(str(i), "Finish!!!")
        i += 1

# fp = open("./KFC.json", mode="a", encoding="utf-8")
# fp.write("}")

fileName = location + "_KFC.json"
fp = open(fileName, mode="a", encoding="utf-8")

json.dump(lst, fp=fp, ensure_ascii=False)

print("over!!!")

