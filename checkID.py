import re


result = re.match(r"(^\d{15}$)|(^\d{18}$)|(^(\d{17})|(\d|X|x)$)", "232303199002124631")

if result == None:
	print("None")
else:
	print(result.string)

result = re.match(r"(^\d{15}$)|(^\d{18}$)|(^(\d{17})|(\d|X|x)$)", "23230319900212X")

if result == None:
	print("None")
else:
	print(result.string)

result = re.match(r"(^\d{15}$)|(^\d{18}$)|(^(\d{17})|(\d|X|x)$)", "23230319900212463X")

if result == None:
	print("None")
else:
	print(result.string)

result = re.match(r"(^\d{15}$)|(^\d{18}$)|(^(\d{17})|(\d|X|x)$)", "2323X3199002124631")

if result == None:
	print("None")
else:
	print(result.string)
