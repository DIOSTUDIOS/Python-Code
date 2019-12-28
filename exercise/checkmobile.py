import re


match = re.match(r"(^13[4-9]\d{8}$)|(^15[01289]\d{8}$)", '13634222222')

if match == None:
	print("None")
else:
	print(match.string)


