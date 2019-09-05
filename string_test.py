str_1 = "我欲乘风归去，又恐琼楼玉宇，高处不胜寒。"
str_2 = "我欲乘风归去，犹恐琼楼玉宇，高处不胜寒，"

# print(len(str_1))
# print(len(str_2))

for number in range(0, len(str_1)):
	# print(number)
	# print(str_1[number], end="")
	if str_1[number] == str_2[number]:
		print(str_1[number], end="")
	else:
		print(str_1[number] + "(" + str_2[number] + ")", end="")

print()
