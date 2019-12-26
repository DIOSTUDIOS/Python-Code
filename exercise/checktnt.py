import re


pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
about = r'我是一名程序员，我喜欢看黑客的图书，项研究一下Trojan'
sub = re.sub(pattern, r'>_<', about)
print(sub)

about = r'我是一名程序员，我喜欢看电脑方面的图书，项研究一下网站'
sub = re.sub(pattern, r'>_<', about)
print(sub)