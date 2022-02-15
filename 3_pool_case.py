# -*- coding = utf-8 -*-
# @Time : 2022/2/13 3:32 PM
# @Author : Jieying Dong (Jessie)
# @File : 3_pool_case.py
# @Software: PyCharm
from lxml import etree
import requests
from multiprocessing.dummy import Pool

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
}

url = "https://www.pearvideo.com/category_5"

page_text = requests.get(url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    vid = li.xpath('./div/a/@href')[0].replace("video_", "")
    video_url = "https://www.pearvideo.com/videoStatus.jsp?contId=" + vid
    name = li.xpath('./div/a/div[2]/text()')[0]
    name_full = name + ".mp4"
    headers['Referer'] = 'https://www.pearvideo.com' + li.xpath('./div/a/@href')[0]
    detail_page_json = requests.get(video_url, headers=headers).json()
    detail_mp4 = detail_page_json['videoInfo']['videos']['srcUrl']
    detail_mp4_1 = detail_mp4.split("/")[-1]
    detail_mp4_2 = detail_mp4_1.split("-")[0]
    # print(detail_mp4_2)
    detail_mp4 = detail_mp4.replace(detail_mp4_2, "cont-" + vid)
    dic = {
        'name': name_full,
        'url': detail_mp4
    }
    urls.append(dic)

def get_videos(dic):
    url = dic['url']
    print(dic['name'] + 'downloading!!!')
    data = requests.get(url, headers=headers).content
    with open(dic['name'], mode="wb") as fp:
        fp.write(data)
        print(dic['name'] + 'successfully!!!!')

pool = Pool(4)
pool.map(get_videos, urls)

pool.close()
pool.join()
