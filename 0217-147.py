
def get_html_lines(html_path):
    f = open(html_path, 'r')
    ls = f.readlines()
    f.close()
    return ls


def extract_image_urls(html_list):
    urls = []
    for line in html_list:
        if 'img' in line:
            url = line.split('https://')[-1].split('.jpeg')[0]
            url = 'https://' + url + '.jpeg'
            # if 'http' in url:
            urls.append(url)
    return urls


def show_results(urls):
    count = 0
    for url in urls:
        print('第{:2}个URL：{}'.format(count, url))
        count += 1


def save_results(file_path, urls):
    f = open(file_path, 'w')
    for url in urls:
        f.write(url+'\n')
    f.close()


def main():
    input_file = 'pic.html'
    output_file = 'pic_url.txt'
    html_lines = get_html_lines(input_file)
    image_urls = extract_image_urls(html_lines)
    show_results(image_urls)
    save_results(output_file, image_urls)


if __name__ == '__main__':
    main()
