from bs4 import BeautifulSoup
import requests


def do_spider(url):

    req = requests.get(url)
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    texts = soup.find('div', class_='showtxt')  # 该网页只有一个div，所以使用find
    # print(texts)
    # texts = texts[0].text.replace('\xa0' * 8, '\n\n')
    text = texts.get_text()

    print(text)
    return texts


if __name__ == '__main__':
    url = 'http://www.biqukan.com/1_1094/17967679.html'
    do_spider(url)
