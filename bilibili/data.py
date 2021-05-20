import requests
from bs4 import BeautifulSoup

RANK = 'https://www.bilibili.com/v/popular/rank/all'

def get_rank():
    resp = requests.get(RANK).text
    soup = BeautifulSoup(resp, features='html.parser')
    videos = soup.select('.rank-item > .content > .info > a')
    print(len(videos))
    for video in videos:
        print(video.attrs['href'][2:], video.get_text())