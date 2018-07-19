# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd
import csv
import re

# import unicodecsv


def get_url(url):
    url_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source  # get html
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    texts = soup.find_all('a')
    for text in texts:
        href = text.get('data-src')
        if href:
            url_list.append(href)
    # for each in url_list:
    #     print(each)
    url_list.pop(10)  # 第10项鞋靴存在莫名问题，暂时pop，之后修改
    return url_list


def do_spider(url):
    com_list = []
    driver = webdriver.Chrome()
    # print(url)
    driver.get(url)
    html = driver.page_source  # get html
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    # print(soup.find_all('div', {'class': 'pro-item m-tag-a '}))
    # print(soup.find_all('p'))
    list_soup = soup.find_all('div',
                              {'class': re.compile('pro-item m-tag-a (.*?)')})
    for com_info in list_soup:
        com_title = com_info.find('p', {'class': 'pro-info'}).string.strip()
        com_desc = com_info.find('p', {'class': 'pro-desc'}).string.strip()
        com_price = com_info.find('span', {'class': 'm-num'}).string.strip()
        com_list.append([com_title, com_desc, com_price])
    # print(com_list)
    driver.close()
    return com_list


def print_lists_csv(com_lists):

    with open('test_1.csv', 'a+', encoding='GB18030', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'info', 'price'])
        writer.writerows(com_lists)
        # w = unicodecsv.writer(csvfile, encoding='utf-8-sig')
        # w.writerows(com_lists)


if __name__ == '__main__':
    # com_lists = do_spider(url[1])
    # if com_lists != None and len(com_lists) >= 1:
    #     print(url[0] + '爬取成功！')
    # print_lists_csv(com_lists)
    url = 'https://youpin.mi.com'
    # get_url(url)
    url_list = get_url(url)
    for each in url_list:
        urls = url + each
        com_lists = do_spider(urls)
        # print_lists_csv(com_lists)
