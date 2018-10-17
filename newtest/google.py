import urllib.request
import time
import pycurl
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def screenImg():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(
        chrome_options=chrome_options,
        executable_path="/Users/yycx/Downloads/chromedriver")
    url = "http://zh.lmgtfy.com/?q=%E5%A4%8D%E5%88%B6%20%E4%BC%B8%E6%89%8B%E9%97%AE%E9%A2%98"
    browser.set_window_size(1200, 600)
    browser.get(url)
    begin = time.time()
    for i in range(0, 30):
        browser.save_screenshot('img/' + str(i) + ".png")
        time.sleep(0.04)
    print(time.time() - begin)
    browser.close()


def getImg(url):
    b = BytesIO()
    c = pycurl.Curl()  # 创建一个curl对象
    c.setopt(pycurl.URL, url)  # 指定请求的URL
    c.setopt(pycurl.WRITEFUNCTION, b.write)  # 回调
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.MAXREDIRS, 0)  # 重定向
    c.setopt(pycurl.CONNECTTIMEOUT, 60)  # 链接超时
    c.perform()  # 运行
    html = b.getvalue()
    return html


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_content, file_path='img'):
    file_name = str(time.time()).replace('.', '')
    with open(file_path + '/' + file_name + ".jpg", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        if (f.write(file_content)):
            print(file_name + '  saved')


def all_file(img_url):
    i = 0
    begin = time.time()
    while i < 120:
        html = getHtml(img_url)
        # html = getImg(img_url)
        # saveHtml(html)
        saveHtml(html, 'img')
        print(i)
        time.sleep(0.04)
        i += 1
    print(time.time() - begin)


if __name__ == '__main__':
    # aurl = "http://192.168.31.4/webcapture.jpg?command=snap&channel=1"
    # aurl = 'http://wx4.sinaimg.cn/mw690/a561b538ly1fw5b4zy8jwj20jn0rs0vd.jpg'
    aurl = 'http://zh.lmgtfy.com/?q=%E5%A4%8D%E5%88%B6%20%E4%BC%B8%E6%89%8B%E9%97%AE%E9%A2%98'
    # aurl = 'http://www.zjut.edu.cn/'
    # all_file(aurl)
    screenImg()
