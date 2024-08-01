# # 带参数请求
# import requests
#
# '''
# 最终拼接效果为：
# https://www.baidu.com/s?wd=Python
# '''
# param = {"wd": "Python"}
# get_url = 'https://www.baidu.com'
# response = requests.get(get_url, params=param)
# print(response.content)


# # 携带Session参数
# import requests
# # s = requests.Session()
# # r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
# # print(r.text)
# # # '{"cookies":{}}'
# with requests.Session() as s:
#    r = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# print(r.text)


# 请求Prepared Request
from requests import Request, Session

s = Session()
url = 'https://www.cnblog.com'
data = {"s": "Golang"}
header = {'Accept-Encoding': 'identity,deflate,compress,gzip', 'Accept': '*/*', 'User-Agent': 'python-requests/0.13.1'}
req = Request('GET', url,
              data=data,
              headers=header,
              )
prepare_obj = req.prepare()
resp = s.send(prepare_obj,
              stream=stream,
              verify=verify,
              cert=cert,
              timeout=timeout
              )
print(resp.status_code)
