# -*- coding：utf-8 -*-
import requests
import json
import os
import random
import socket
# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(10)


def baidu_pic_url(num, keyword):
    pic_url = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    for i in range((num // 48) + 1):
        page_url = 'https://pic.sogou.com/pics?query={}&mode=1&start={}&reqType=ajax&reqFrom=result&tn=0'.format(keyword, i*48)
        r = requests.get(page_url, headers=headers).text
        res = json.loads(r)['items']
        if res:
            for j in res:
                try:
                    url = j['hoverURL']
                    pic_url.append(url)
                except:
                    pass
    print(len(pic_url))
    return pic_url


def down_img(num, keyword):
    pic_url = baidu_pic_url(num, keyword)
    if os.path.exists('D:/图片/'+keyword):
        pass
    else:
        os.makedirs('D:/图片/'+keyword)

    path = 'D:/图片/'
    for index, i in enumerate(pic_url):
        try:
            filename = path + keyword + '/' + str(index) + '.jpg'
            print(filename)
            with open(filename, 'wb+') as f:
                f.write(requests.get(i).content)
        except:
            continue


if __name__ == '__main__':
    keyword = '大海'
    num = int(input('请输入爬取图片数目：'))
    down_img(num, keyword)

