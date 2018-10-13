import urllib.request
import time
import pycurl
from io import BytesIO


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


def saveHtml1(file_content, file_path='img', file_name='1'):
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
        saveHtml1(html, 'test', str(i))
        print(i)
        time.sleep(0.04)
        i += 1
    print(time.time() - begin)


if __name__ == '__main__':
    # aurl = "http://192.168.31.4/webcapture.jpg?command=snap&channel=1"
    aurl = 'http://wx4.sinaimg.cn/mw690/a561b538ly1fw5b4zy8jwj20jn0rs0vd.jpg'
    # aurl = 'http://www.zjut.edu.cn/'
    all_file(aurl)
    # print(getHtml(aurl))
    # print(getImg(aurl))
