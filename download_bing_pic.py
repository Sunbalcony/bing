import requests
import re


class Bing:
    url = 'http://cn.bing.com/HPImageArchive.aspx?idx=20&n=10' #xml
    # url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN' #json

    def get_url(self):
        respon = requests.get(Bing.url)
        res = respon.text
        re_respon = re.findall(r'<url>(.*?)</url>', res, re.S | re.M)
        i = 1
        for url in re_respon:
            burl = 'http://cn.bing.com' + url
            img = requests.get(burl)
            # print(img.content)
            filename = str(i) + '.' + 'jpg'
            f = open(filename, 'wb+')  #ab
            f.write(img.content)
            f.close()
            print(i)
            i += 1


p = Bing()
p.get_url()
