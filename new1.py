from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    chrome_options=chrome_options,
    executable_path="/Users/yycx/Downloads/chromedriver")
url = "http://iwebshop.spider.com/index.php?controller=site&action=products&id={}"
# url = "http://www.dysfz.cc/movie24099.html"
for i in range(1, 10):
    tmp_url = url.format(i)
    driver.get(tmp_url)
    html = driver.page_source
    # print(html.encode("utf8"))
    file_name = "./page/myhtml_{}.html".format(i)
    with open(file_name, "w+", encoding="utf-8") as f:
        f.write(html)
        f.close()
