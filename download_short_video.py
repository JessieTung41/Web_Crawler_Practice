# -*- coding = utf-8 -*-
# @Time : 2022/1/28 7:04 PM
# @Author : Jieying Dong (Jessie)
# @File : 3_3_anti-theft chain.py
# @Software: PyCharm

# 1. get contId
# 2. get videoStatus
# 3. change srcUrl
# 4. download the video

import requests
url = "https://www.pearvideo.com/video_1750540"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    # anti-theft chain: backtracking
    "Referer": url
}
resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, "cont-"+ contId)

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

