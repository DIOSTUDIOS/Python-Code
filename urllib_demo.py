import urllib.request
import urllib.parse


# response = urllib.request.urlopen(r"http://www.baidu.com")
# html = response.read()
# print(html)

data = bytes(urllib.parse.urlencode({"word":"hello"}), encoding="utf-8")
response = urllib.request.urlopen(r"http://httpbin.org/post", data=data)
html = response.read()
print(html)