'''
发现-知乎 热门话题爬取。使用requests库和lxml的xpath解析。
'''
import requests
from lxml import etree


url = 'https://www.zhihu.com/explore'


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(text):
    html = etree.HTML(text)
    daily = html.xpath(
        '//div[@data-type="daily"]/div[contains(@class, "feed-item")]',
    )
    result = []
    for item in daily:
        title = item.xpath('h2/a/text()')
        answer = item.xpath(
            'div/div[@class="answer-head"]/div/span/span/'
            'a[@class="author-link"]/text()',
        )
        content_parse = item.xpath(
            'div/div[contains(@class, "zm-item-rich-text")]/textarea/text()',
        )
        # xpath获取的元素下面text 是被几个标签分割开的，想要一次性全部获取，使用string(.)
        content = etree.HTML(content_parse[0]).xpath(
            'string(.)',
        ) if content_parse else ''
        result.append([title[0].strip(), answer[0].strip(), content])
    return result


def write_to_file(result):
    with open('zhihu.txt', 'a') as f:
        for item in result:
            f.write('\n'.join(item))
            f.write('\n' + '===' * 20 + '\n')


def main():
    html = get_page(url)
    result = parse_page(html)
    write_to_file(result)


if __name__ == '__main__':
    main()
