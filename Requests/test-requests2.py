import requests

url = 'https://pics0.baidu.com/feed/267f9e2f0708283839f8f0894736720f4e08f1f0.jpeg@f_auto?token=de27064d20a6d947facdb2277cf90cc8'
response = requests.get(url=url)
code = response.content

with open('test.jpg', 'wb') as f:
    f.write(code)