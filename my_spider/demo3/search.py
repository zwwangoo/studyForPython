from pages import get_response
from params import SearchRequests


def get_search_result(key):
    '''
    获取关键字搜索Ajax异步接口返回的json数据
    '''
    requests_params = SearchRequests(key)
    response = get_response(requests_params, 'json')
    return response


def get_detail_url(result):
    '''
    分析返回的json数据，处理搜索结果的跳转链接
    '''

    docs = result.get('result', {'response': {'docs': []}}).get(
        'response',
    ).get('docs')
    for item in docs:
        name = item['name']
        id = item['id']
        location = item['location'][:-3]
        url = item['domain'] + \
            '/Homo_sapiens/Gene/Summary?db=core;g={};r={}'.format(id, location)
        yield {
            'name': name,
            'location': location,
            'url': url,
        }
