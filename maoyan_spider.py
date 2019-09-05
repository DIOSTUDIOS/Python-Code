import requests
import re


def get_one_page(url):
	response = requests.get(url)

	if response.status_code == 200:
		return response.text
	else:
		return None


def parse_one_page(html):
	pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>', re.S)

	item = re.findall(pattern, html)
	print(item)


if __name__ == "__main__":
	html = get_one_page("https://maoyan.com/board/4")
	
	parse_one_page(html)