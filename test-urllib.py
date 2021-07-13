# _*_ xoding: utf-8 _*_
#urllib
from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        if not f.staus ==200: raise ValueError('请求失败')
        return {'query': data.decpde('utf-8')}

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')