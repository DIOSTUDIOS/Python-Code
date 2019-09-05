import requests
import re

url = r'https://maoyan.com/board'


def get_file_name():
	response = requests.get(url=url)
	pattern = r'<a href="/films/\d+" title=".*?" data-act="boarditem-click" data-val="{movieId:\d+}">(.*?)</a>'
	files = re.findall(pattern=pattern, string=response.text, flags=re.I)

	return files


def get_file_image():
	i = 0
	files = get_file_name()

	response = requests.get(url=url)
	pattern = r'<img data-src="(.*?)@160w_220h_1e_1c" alt=".*?" class="board-img" />'
	imgs = re.findall(pattern=pattern, string=response.text, flags=re.I)

	for img_url in imgs:
		image = requests.get(url=img_url).content
		with open(files[i] + '.jpg', 'wb') as file:
			file.write(image)

		i = i + 1


if __name__ == '__main__':
	get_file_image()
