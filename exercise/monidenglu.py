import requests
from lxml import etree
import re


class Login:
	def __init__(self):
		self.headers = {
			'Referer': 'https://github.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
			'host': 'github.com'
		}
		self.login_url = 'https://github.com/login'
		self.post_url = 'https://github.com/session'
		self.logined_url = 'https://github.com/setting/profile'
		self.session = requests.Session()

	def token(self):
		response = self.session.get(self.login_url, headers=self.headers)
		# selector = etree.HTML(response.text)
		# token = selector.xpath('/html/body/div[1]/header/div[3]/nav/form/input[2]/@value')

		pattern = r'<input type="hidden" name="authenticity_token" value="(.*?)" />'
		token = re.findall(pattern, response.text, re.S)
		
		return token[0]

	def login(self, email, password):
		post_data = {
			'commit': 'Sign in',
			'utf8': '✓',
			'authenticity_token': self.token(),
			'login': email,
			'password': password
		}

		response = self.session.get(self.post_url, data=post_data, headers=self.headers)
		if response.status_code == 200:
			print('abcdef')

		response = self.session.get(self.login_url, headers=self.headers)
		if response.status_code == 200:
			print("123456")


if __name__ == '__main__':
	login = Login()
	# token = login.token()
	# print(token)
	login.login(email='personalmail.wang@icloud.com', password='W4585z5430q3931?')