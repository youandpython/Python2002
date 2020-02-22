# coding=utf-8
import requests
from bs4 import BeautifulSoup
import time
import random

num = int(input('please input the page number:'))
page_urls = []
i = 0
for page in range(1, num+1):
    time.sleep(random.random())
    url_ = f'http://forum.home.news.cn/list/50-0-0-{page}.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    print(f'the page {page} crawling.........')
    r = requests.get(url_, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    titles = soup.find_all('a', 'bt')
    for title in titles:
        # try:
        i += 1
        title = title.get_text()
        time.sleep(0.2)
        print(str(i)+'.'+title)
        with open('news_title.txt', 'a', encoding='utf-8') as f:
            # f.write(str(i)+'.'+title+'\n')
            f.write(title+'\n')
        # except:
        #     pass

