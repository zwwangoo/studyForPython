# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request, FormRequest
from scrapy.http.cookies import CookieJar

cookie_jar = CookieJar()


class HuaxuejiaSpider(scrapy.Spider):
    name = 'huaxuejia'
    allowed_domains = ['huaxuejia.cn']
    start_urls = ['2622-83-5']
    search_index = 'http://data.huaxuejia.cn/search.php'

    def start_requests(self):

        for cas in self.start_urls:
            self.cas = cas
            yield FormRequest(self.search_index, method='POST',
                              formdata={'search_keyword': cas},
                              callback=self.request1)

    def request1(self, response):

        yield FormRequest.from_response(response, method='POST',
                                        formdata={'search_keyword': self.cas},
                                        clickdata={'name': 'submit'},
                                        callback=self.request2)

    def request2(self, response):

        action = re.search(r'http://(.*?)\.html', response.text)
        url = action.group(0)
        print('url--------------------')
        print(url)
        yield Request(url, method='GET',
                      headers={'Cookie': response.headers.getlist('Set-Cookie')},
                      dont_filter=True,
                      callback=self.parse)

    def parse(self, response):
        base_info = response.xpath(
            '//div[@id="baseInfo"]/div/dl[@class="dl-horizontal"]')

        base_info = base_info[0]

        keys = base_info.xpath('dt/text()').extract()
        cas_base_info = {}
        for index, key in enumerate(keys):
            cas_base_info[key.split('：')[0]] = base_info.xpath(
                'string(dd[{}])'.format(index + 1)).extract_first()

        phychem_info = response.xpath(
            '//div[@id="phyChem"]/div/dl[contains(@class, "dl-horizontal")]')
        if len(phychem_info) > 0:
            phychem_info = phychem_info[0]
            keys = phychem_info.xpath('dt/text()').extract()
            for index, key in enumerate(keys):
                cas_base_info[key.split('：')[0]] = phychem_info.xpath(
                    'string(dd[{0}]/b|dd[{0}])'.format(index + 1)).extract_first()

            more = cas_base_info.pop('其它信息', '').strip()
            if more:
                cas_base_info['更多'] = re.sub(r'\[\d.?\]', '', more)

            cas_base_info['存储条件/存储方法'] = re.sub(r'\s|\[\d.?\]',
                                                '', cas_base_info.get('存储条件/存储方法', ''))

        # MSDS
        cas_base_info['稳定性相关'] = re.sub(
            r'\s|\[\d.?\]', '', cas_base_info.get('稳定性相关', ''))
        # msds = response.xpath('//div[@id="chemMsds"]')
        # if len(msds) > 0:
        #     cas_base_info['MSDS'] = etree.tostring(
        #         msds[0], encoding='utf-8').decode()

        # 合成线路
        # synRoute = response.xpath('//div[@class="synRoute"]')
        # route_items = ''
        # for syn in synRoute:
        #     line = syn.xpath('ul/li')
        #     for item in line:
        #         if 'synR_arrow' in item.get('class'):
        #             route_items += ','.join(item.xpath('p/text()').extract()) + ' '
        #         else:
        #             route_items += ':'.join(item.xpath('p/text()').extract()) + ' '
        #     route_items += '\n'
        # cas_base_info['合成线路'] = route_items

        # 上下游产品

        up_down_products = ''
        ud_stream = response.xpath('//div[@id="upDownPro"]/div/ul')
        if len(ud_stream) > 1:
            for index, value in enumerate(['上游产品：', '下游产品：']):
                up_stream = ud_stream[index].xpath('li')
                up_down_products += value
                for item in up_stream:
                    up_down_products += ':'.join(item.xpath('p/text()').extract()) + '|'
                up_down_products += '\n'
        cas_base_info['上下游产品'] = up_down_products

        # 分子结构和计算化学数据
        ip_deslist = response.xpath('//div[@id="dataStruc"]//dl[@class="ip_deslist"]')
        for des in ip_deslist:
            title = des.xpath('string(preceding-sibling::h3[1]/span)')
            if title in ['分子结构数据', '计算化学数据']:
                content = [i for i in des.xpath('p/text()').extract() if i.strip()]
                if len(content) > 0:
                    cas_base_info[title] = '\n'.join(content)
                else:
                    cas_base_info[title] = des.xpath('string(.)').strip()

        # 删除无关项
        cas_base_info.pop('油水分配系数/LogP', '')
        cas_base_info.pop('3D弹球模型', '')
        cas_base_info.pop('InChI', '')

        yield cas_base_info
