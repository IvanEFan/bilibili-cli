import json

import requests
from bs4 import BeautifulSoup
from rich.text import Text

VIDEO_API = 'https://api.bilibili.com/x/web-interface/archive/stat?bvid='
DETAIL_API = 'https://api.bilibili.com/x/web-interface/view/detail?aid='
RANK = 'https://www.bilibili.com/v/popular/rank/all'

PLAYER_BASE = 'https://www.bilibili.com/video/'

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

class Video:
    def __init__(self, bv: str):
        self.bv = bv
        self.link = PLAYER_BASE + self.bv
        resp = requests.get(VIDEO_API + self.bv, headers=HEADER).text
        data = json.loads(resp)
        if data['code'] == 0:
            data = data['data']
            self.aid = data['aid']
            self.view = data['view']
            self.danmaku = data['danmaku']
            self.favorite = data['favorite']
            self.coin = data['coin']
            self.like = data['like']
            detail_resp = requests.get(DETAIL_API + str(self.aid), headers=HEADER).text
            detail = json.loads(detail_resp)
            if detail['code'] == 0:
                detail = detail['data']
                self.desc = detail['View']['desc']
                self.title = detail['View']['title']
                self.up = detail['View']['owner']['name']

    def get_formatted(self):
        # idk why i cant pass 'style' directly in to the Text object
        title = Text(self.title)
        title.stylize(f'link {self.link}')
        return {
            'title': title,
            'stats': Text(f'👀{self.view} 👍{self.like} 🔵{self.coin} ⭐{self.favorite}'),
            'up': Text(self.up),
            'desc': Text(self.desc if self.desc else 'no description')
        }

def get_rank(count=15):
    resp = requests.get(RANK).text
    soup = BeautifulSoup(resp, features='html.parser')
    videos = soup.select('.rank-item > .content > .info > a')
    # print(len(videos))
    results = []
    for index, video_element in enumerate(videos):
        if index == count:
            break
        # print(video_element.attrs['href'][25:], video_element.get_text())
        video = Video(video_element.attrs['href'][25:])
        results.append(video)
    return results