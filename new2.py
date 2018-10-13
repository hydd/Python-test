from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    chrome_options=chrome_options,
    executable_path="/Users/yycx/Downloads/chromedriver")
count = 0
for i in range(1, 6):
    url = "http://zblog.spider.com/page/{}/".format(i)
    driver.get(url)
    main_html = driver.page_source
    # print(main_html.encode("utf-8"))
    urls = re.findall(r"http://zblog.spider.com/post/.+?\.html", main_html)
    # print(urls)
    for post_url in urls:
        driver.get(post_url)
        count += 1
        print(driver.title.encode("utf8"))
print(count)
