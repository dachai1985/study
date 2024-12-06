import requests

url = 'http://edu.service.yiguanedu.com/API/getSpecialtyList'
data = {  #data是post参数的写法， params是get参数的写法
    'years':'2024'
}
reponse = requests.get(url=url, data=data)
body = reponse.text #返回结果是字符串，不方便使用
print(body)
print(type(body))

dt = reponse.json() #返回结果是字符串，不方便使用
print(dt)
print(dt['message'])