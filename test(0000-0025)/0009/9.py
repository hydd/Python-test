from bs4 import BeautifulSoup
import requests


def do_spider(url):
    # text = []
    req = requests.get(url)
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    texts = soup.find_all('a')  # 该网页只有一个div，所以使用find
    # print(texts)
    # texts = texts[0].text.replace('\xa0' * 8, '\n\n')
    # text = texts.get_text()
    for each in texts:
        href = each.get('href')  # bs4官方文档首页就有，对bs4常用方法还是不够熟悉
        print(href)
        # text.append(href)

    # print(texts)
    return texts


if __name__ == '__main__':
    url = 'http://www.biqukan.com/1_1094/17967679.html'
    do_spider(url)
