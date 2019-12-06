import requests
import gevent
import time
from lxml import etree
from gevent import monkey
monkey.patch_all()


def callbackf(response):
    html = etree.HTML(response.text)
    print(html.xpath('//title/text()'))


def f(url):
    data = requests.get(url)
    return callbackf(data)


start = time.time()
url_list = []
for i in range(10):
    url_list.append(gevent.spawn(f, 'https://www.bing.com/'))

gevent.joinall(url_list)
print(time.time() - start)
