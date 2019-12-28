import re


pattern = r'\s*@'
string = r'@明日科技 @扎克伯格 @俞敏洪'
list1 = re.split(pattern, string)

for item in list1:
	if item != '':
		print(item)
