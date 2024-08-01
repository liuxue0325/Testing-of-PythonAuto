import requests as rq
response=rq.get("https://www.baidu.com")

if response.status_code==200:
    print("Request is OK")
elif response.status_code==404:
    print("The page is not found")
elif response.status_code>=500:
    print("Server has something wrong!")