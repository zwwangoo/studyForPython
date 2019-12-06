# 引入所需库
import os
import re
import threading
from queue import Queue
import requests
from lxml import etree


class Producer(threading.Thread):
    """
    生产者 - 手机表情包图片地址
    """

    def __init__(self, page_queue, img_queue):
        super(Producer, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        """
        请求 解析 下载
        :param url:
        :return:
        """
        # 声明定义请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        req = requests.get(url=url, headers=headers)
        html = req.text
        tree = etree.HTML(html)
        imgs = tree.xpath(
            '//div[@class="page-content text-center"]//img[@class!="gif"]')
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\??\..,!!\*]]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            file_name = alt + suffix
            self.img_queue.put((img_url, file_name))


class Consumer(threading.Thread):
    """
    消费者 - 下载表情包图片
    """

    def __init__(self, page_queue, img_queue):
        super(Consumer, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        # 声明定义请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, file_name = self.img_queue.get()
            req_img = requests.get(url=img_url, headers=headers)
            with open('images/' + file_name, 'wb') as fp:
                fp.write(req_img.content)
            print(file_name + '下载完成...')


def main():
    """
    主函数
    :return:
    """
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    # 定义五个生产者
    for x in range(6):
        t = Producer(page_queue=page_queue, img_queue=img_queue)
        t.start()

    # 定义三个消费者
    for x in range(4):
        t = Consumer(page_queue=page_queue, img_queue=img_queue)
        t.start()


if __name__ == '__main__':
    main()
