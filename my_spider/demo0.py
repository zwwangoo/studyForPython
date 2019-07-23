from urllib import request, parse

url = 'http://www.python.org'
response = request.urlopen(url)
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
response1 = request.urlopen('http://httpbin.org/post', data=data)
print(response1.read().decode('utf-8'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org',
}

data = bytes(
    parse.urlencode({
        'name': 'Germey',
    }), encoding='utf-8',
)

req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
