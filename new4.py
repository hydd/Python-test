# -*- coding: UTF-8 -*-
import requests
# import json
# url = "http://bianquan.spider.com/servers/public/index.php/index"

url = "https://youpin.mi.com/app/shop/pipe"

# data = {"act": "getPage", "page": 0, "tag": ""}
data = "data=%7B%22detail%22%3A%7B%22model%22%3A%22Shopv2%22%2C%22action%22%3A%22getDetail%22%2C%22parameters%22%3A%7B%22gid%22%3A%22103335%22%7D%7D%2C%22comment%22%3A%7B%22model%22%3A%22Comment%22%2C%22action%22%3A%22getList%22%2C%22parameters%22%3A%7B%22goods_id%22%3A%22103335%22%2C%22orderby%22%3A%221%22%2C%22pageindex%22%3A%220%22%2C%22pagesize%22%3A3%7D%7D%2C%22activity%22%3A%7B%22model%22%3A%22Activity%22%2C%22action%22%3A%22getAct%22%2C%22parameters%22%3A%7B%22gid%22%3A%22103335%22%7D%7D%7D"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
px = {"https": "127.0.0.1:8080"}

r = requests.post(
    url,
    proxies=px,
    verify=r"/Users/yycx/Downloads/PortSwigger.pem",
    data=data,
    headers=headers)

# req = requests.post(url, data=data, headers=headers)
s = r.text
# res = json.loads(s)
# print(res)
print(s.encode("utf8"))
# print(req.text.encode("utf8"))