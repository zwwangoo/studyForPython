import json
import requests
from bs4 import BeautifulSoup


BASE_URL = 'http://pic.haibao.com/hotimage/'
MORE_IMG_URL = 'http://pic.haibao.com/ajax/image:getHotImageList.json'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}


def get_json(url, skip=None):
    params = {}
    if skip:
        params.update({'skip': (None, skip)})
    req = requests.post(url, files=params, headers=HEADERS)
    try:
        req.raise_for_status()
    except Exception as err:
        print('error-----------')
        print(err)
        return ''

    req.encoding = 'utf-8'
    result = json.loads(req.text)
    page = result.get('result').get('html')
    return page


def get_src(html):
    soup = BeautifulSoup(html, 'html.parser')

    img_lable = soup.find_all('img', attrs={'class': 'lazys'})
    for img in img_lable:
        img_src = img.get('data-original')
        print(img_src)
    if len(img_lable) == 0:
        skip = 0
    else:
        skip = img_lable[-1].get('accessurl').split('=')[-1]

    if skip != 0:
        html = get_json(MORE_IMG_URL, skip)
        get_src(html)
    else:
        print('End!')
        return


if __name__ == '__main__':
    html2 = get_json(MORE_IMG_URL)
    get_src(html2)
