import requests


url = r"https://www.baidu.com/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

response = requests.get(url, headers=headers)
print(response.content)

