import re


pattern = r"[1-9]{1,3}(\.[0-9]{1,3}){3}"
str1 = "127.0.0.1 192.168.1.66"
match = re.findall(pattern, str1)
print(match)


pattern = r"([1-9]{1,3})((\.[0-9]{1,3}){3})"
str2 = "127.0.0.1 192.168.1.66"
match = re.findall(pattern, str2)

print(match[0])

# for i in range(2):
# 	print(match[i])