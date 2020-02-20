from bs4 import BeautifulSoup
import requests
import os


def get_html_code(url):
    headers = {'User-Agent': 'MMozilla/5.0(Windows NT 6.1; WOW64; rv:31.0) Gecko20100101 Firefox/31.0'}
    r = requests.get(url, headers=headers)
    r.encoding = 'UTF-8'
    page = r.text
    return page


def get_img(page, local_path, url):
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    soup = BeautifulSoup(page, 'html.parser')
    img_list = soup.find_all('img')
    x = 0
    for img_url in img_list:
        try:
            if 'http://' not in img_url.get('src'):
                m = url+img_url.get('src')
                print('正在下载：%s' % m)
                ir = requests.get(m)
            else:
                print('正在下载：%s' % img_url.get('src'))
                ir = requests.get(img_url.get('src'))
            open(local_path+'%d.jpg' % x, 'wb').write(ir.content)
            x += 1
        except:
            continue


if __name__ == '__main__':
    url = 'http://www.zcinfo.net/pic/'
    local_path = 'E:\\computer\\imgs\\'
    page = get_html_code(url)
    get_img(page, local_path, url)
