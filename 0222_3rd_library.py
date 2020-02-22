# pip, PyInstaller，这是第一节的内容，基础知识，几乎涉及不到代码。
"""
下面是第二节
"""
import requests
from bs4 import BeautifulSoup
import time
import random
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

num = int(input('Please input the total number of pages:'))
page_urls = []
i = 0
for page in range(1, num+1):
    time.sleep(random.uniform(1.5, 3.5))
    url_ = f'http://forum.home.news.cn/list/50-0-0-{page}.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    print(f'the page {page} crawling.........')
    r = requests.get(url_, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    titles = soup.find_all('a', 'bt')
    for title in titles:
        i += 1
        title = title.get_text()
        time.sleep(0.5)
        print(str(i)+'.'+title)
        with open('news_title.txt', 'a', encoding='utf-8') as f:
            f.write(title+'\n')

"""
下面是第三节。
"""
with open('news_title.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = jieba.lcut(text)
new_text = ' '.join(words)
excludes = {'这些', '注意', '如何', '怎么', '什么', '为什么', '开展', '不能', '作者', '陈季', '还是', '七绝', '我们'}
word_cloud = WordCloud(font_path='msyh.ttc',
                       width=1600,
                       height=900,
                       background_color='white',
                       stopwords=excludes,
                       max_words=600).generate(new_text)
word_cloud.to_file('word_cloud.png')

"""
下面是第四节。
"""
with open('news_title.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = jieba.lcut(text)
new_text = ' '.join(words)
counts = {}
excludes = ['这些', '注意', '如何', '怎么', '什么', '为什么', '开展', '不能', '作者', '陈季', '还是', '七绝', '我们']
for word in words:
    if len(word) == 1:
        continue
    elif not ('\u4e00' <= word <= '\u9fff'):
        continue
    elif word in excludes:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
use_dic = {}
for item in range(10):
    use_dic[items[item][0]] = items[item][1]
plt.rcParams['font.sans-serif'] = ['SimHei']
labels = use_dic.keys()
data = use_dic.values()
explode = (0.1, 0.01, 0.1, 0.02, 0.1, 0.1, 0.01, 0.1, 0.02, 0.1)
plt.title('高频词饼状图')
plt.pie(data, labels=labels, explode=explode, autopct='%1.1f%%')
plt.savefig('word_pie.png')
plt.show()
plt.bar(labels, data)
plt.title('高频词柱状图')
plt.savefig('word_bar.png')
plt.show()








