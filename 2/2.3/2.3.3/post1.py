import requests, json

# 常用用法
url = 'http://httpbin.org/post'
data = {'key1''value1', 'key2':'value2'}
r = requests.post(url.data)
print(r)
print(r.text)
print(r.content)

