import urllib3


http = urllib3.PoolManager()
response = http.request("GET", "http://www.baidu.com")
print(response.data)