# coding=utf-8
import requests
from bs4 import BeautifulSoup
import time
import random
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
# page_urls = []
# j = 0
# for page in range(1, 101):
#     time.sleep(random.random())
#     url_ = f'http://bbs1.people.com.cn/board/1/1_{page}.html'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
#     print(f'the page {page} crawling.........')
#     r = requests.get(url_, headers=headers).text
#     soup = BeautifulSoup(r, 'html.parser')
#     titles = soup.find_all(class_='treeReplyItem')
#     for u in titles:
#         a = u.find('p', class_="treeTitle").find('a', class_="treeReply")
#         print(a)
#     exit()
#     for i in range(len(titles)):
#         j += 1
#         title = titles[i].p.a.text.replace('\t', '').replace(' ', '').replace('\n', '').replace('\r', '')
#         print(str(j) + '.' + title)
#         with open('_titles.txt', 'a', encoding='utf-8') as f:
#             f.write(str(j) + '.' + title + '\n')

with open('news_title.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')

words = jieba.lcut(text)
new_text = ' '.join(words).replace('这些', '').replace('如何', '').replace('这些', '').replace('如何', '').replace('怎么', '')
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif not ('\u4e00' <= word <= '\u9fff'):
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in items:
    print(i[0], i[1])

image = Image.open('e://dang.jpg')
mask = np.array(image)

word_cloud = WordCloud(font_path='msyh.ttc',
                       width=1600,
                       height=900,
                       mask=mask,
                       background_color='white',
                       max_words=600).generate(new_text)

word_cloud.to_file('word_cloud.png')
