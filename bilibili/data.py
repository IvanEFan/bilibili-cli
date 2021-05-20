import json

import requests
from bs4 import BeautifulSoup

VIDEO_API = 'https://api.bilibili.com/x/web-interface/archive/stat?bvid='
RANK = 'https://www.bilibili.com/v/popular/rank/all'

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

class Video:
    def __init__(self, bv: str, title: str):
        self.bv = bv
        self.title = title
        resp = requests.get(VIDEO_API + self.bv, headers=HEADER).text
        data = json.loads(resp)
        data = data['data']
        self.view = data['view']
        self.danmaku = data['danmaku']
        self.favorite = data['favorite']
        self.coin = data['coin']

def get_rank():
    resp = requests.get(RANK).text
    soup = BeautifulSoup(resp, features='html.parser')
    videos = soup.select('.rank-item > .content > .info > a')
    print(len(videos))
    results = []
    for video_element in videos:
        print(video_element.attrs['href'][25:], video_element.get_text())
        video = Video(video_element.attrs['href'][25:], video_element.get_text())
        results.append(video)
    return results