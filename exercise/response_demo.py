import requests


response = requests.get(url=r'https://maoyan.com/board')
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.url)
print(response.history)