import requests

url = "https://www.baidu.com"
headers = {
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
params = {
    'id':10
}
response = requests.get(url=url, headers=headers, params=params) 
# response相应对象，从这个对象中可以获取我们想要的响应信息
print(response)
print(response.status_code)
print(response.encoding) #响应头字符编码

response.encoding = 'utf-8'
print(response.url) #请求url
print(response.cookies)

# print(response.text)  #html源码

print(response.content) #字节形式的响应内容
print(response.json) #json形式的响应内容

