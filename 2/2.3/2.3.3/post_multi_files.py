# import requests, json
#
# url = 'http://httpbin.org/post'
# files = {'file': open('./report.txt', 'rb')}
# # 设置要被打开的文件
# res = requests.post(url_mul, files=files)
# # 发送POST请求
# print(res)
# print(res.text)
# print(res.content)

import requests, json

url = 'http://httpbin.org/post'
multiple_files = [('images', ('test1.png', 'test2.png', 'rb'), 'impage/png')]
response = requests.post(url, files=multiple_files)
print(response.text)
