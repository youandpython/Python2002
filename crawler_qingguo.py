# coding=utf-8
import requests
from bs4 import BeautifulSoup
import time
import random
page_urls = []
j = 0
for page in range(1, 101):
    time.sleep(random.random())
    url_ = f'http://bbs1.people.com.cn/board/1/1_{page}.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    print(f'the page {page} crawling.........')
    r = requests.get(url_, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    titles = soup.find_all(class_='treeReplyItem')
    for i in range(len(titles)):
        j += 1
        # title = titles[i].p.a.text.replace('\t', '').replace(' ', '').replace('\n', '').replace('\r', '')
        title = titles[i].p.a.get_text().strip()
        print(str(j) + '.' + title)
        with open('_titles.txt', 'a', encoding='utf-8') as f:
            f.write(str(j) + '.' + title + '\n')

