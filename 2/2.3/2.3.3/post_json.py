import requests, json

url_json = 'http://httpbin.org/post'
# dumps：可以将Python对象解码为JSON数据
data_json = json.dumps({'stock_no': '600585', 'price': '52.12'})
res = requests.post(url_json, data_json)
print(res)
print("*"*50)
print(res.text)
print("*"*50)
print(res.content)
