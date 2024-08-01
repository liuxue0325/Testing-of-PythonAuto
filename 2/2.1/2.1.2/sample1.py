# -*-coding:utf-8-*-
import requests

# 引入requests库
# 使用GET方式请求百度首页
response = requests.get("https://www.baidu.com/")
# print(response)
# # 打印响应对象

# # 查看响应内容，response.text为Unicode格式的数据
# print(response.text)
# # 查看响应数据内容，response.content为字节流数据
# print(response.content)
# # 查看完整的URL地址
# print(response.url)
# # 查看响应头部字符编码
# print(response.encoding)
# # 查看响应码
# print(response.status_code)

# import urllib.request
# # 获取一个HTTP响应对象
# response=urllib.request.urlopen('https://www.baidu.com')
# print(response)

if response.status_code == 200:
    print(response.text,'\n{}\n'.format('*'*79),response.encoding)
    response.encoding = 'GBK'
    #存储结果或者对比结果
else:
    print("fail")