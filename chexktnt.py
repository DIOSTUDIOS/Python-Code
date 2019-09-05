import re


pattern = r"(黑客)|(抓包)|(监听)|(Trojan)"
about = r"我是一个程序员，我喜欢看黑客方面的书，想研究一下Trojan"
match = re.search(pattern, about)
if match == None:
	print("Yes")
else:
	print("No")

pattern = r"(黑客)|(抓包)|(监听)|(Trojan)"
about = r"我是一个程序员，我喜欢看计算机方面的书，我想开发网站"
match = re.search(pattern, about)
if match == None:
	print("Yes")
else:
	print("No")