from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import re
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    chrome_options=chrome_options,
    executable_path="/Users/yycx/Downloads/chromedriver")

url = "http://zblog.spider.com/post/kepuzhan.html"  # 注意带入当前页面的url
driver.get(url)
html = driver.page_source
all_li = BeautifulSoup(html, "lxml").find_all(attrs={"class": "post single"})
for li in all_li:
    title = li.find("h2").text.strip()
    time = li.find('h4').text.strip()
    body = li.find('p').text.strip()
    author_browser_comment = li.find('h6').text.strip()
    print('{} {} {} {}'.format(title, time, body,
                               author_browser_comment).encode("utf8"))
    driver.quit()
