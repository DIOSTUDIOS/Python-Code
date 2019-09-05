import re


match_obj = re.match("www", "www.baidu.com")

if match_obj:
	print(match_obj.group())
else:
	print("NOTHING MATCHED")

print(re.match("com", "www.baidu.com"))
