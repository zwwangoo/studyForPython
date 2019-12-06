# -*- coding: utf-8 -*-
import scrapy
from cas_spider.items import CasSpiderItem


class CasSpider(scrapy.Spider):
    name = 'cas'
    allowed_domains = ['www.cphi.cn']
    start_urls = ['https://www.cphi.cn/cas/index.php?num=1&page=1']
    # handle_httpstatus_list = [403]

    def parse(self, response):

        if response.status == 403:
            return

        rows = response.xpath('//table[@id="m-tab"]/tbody/tr')

        base_url, args = response.url.split('?')
        num, page = args.split('&')
        num, page = int(num.split('=')[-1]), int(page.split('=')[-1])

        if len(rows) < 1:
            if num > 9:
                return
            num += 1
            page = 1
        else:
            page += 1
        next_url = '{}?num={}&page={}'.format(base_url, num, page)
        print('----------------', next_url)

        for row in rows:
            cas_info = CasSpiderItem()
            cas_info['cas'] = row.xpath('string(td[1]/a)').extract_first()
            cas_info['enname'] = row.xpath('string(td[2])').extract_first()
            cas_info['as_enname'] = row.xpath('string(td[3])').extract_first()
            cas_info['zhname'] = row.xpath('string(td[4])').extract_first()
            cas_info['as_zhname'] = row.xpath('string(td[5])').extract_first()

            cas_info['cas_href'] = row.xpath('td[1]/a/@href').extract_first()
            yield cas_info

        yield scrapy.Request(next_url,
                             headers={'Cookie': response.headers.getlist('Set-Cookie')},
                             callback=self.parse)
