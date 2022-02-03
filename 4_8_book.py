# -*- coding = utf-8 -*-
# @Time : 2022/1/31 10:36 AM
# @Author : Jieying Dong (Jessie)
# @File : 4_8_book.py
# @Software: PyCharm

# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} ==> all chapters content(name,cid)
# a chapter content
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import json
import aiofiles

# 1. sync execution: browse getCatalog (get all chapters cid and name)
# 2. async execution: browse getChapterContent (download all chapters content)

async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("book/"+title, mode="w") as f:  # aiofiles
                await f.write(dic["data"]["novel"]["content"])



async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    # print(dic)
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # prepare asyn execution
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    asyncio.run(getCatalog(url))

