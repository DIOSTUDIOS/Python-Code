def func_bmi(person, height, weight):
	print(person + "的身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")

	bmi = weight/(height**2)

	print(person + "的BMI指数为：" + str(bmi))

	if bmi < 18.5:
		print("偏瘦")
	elif bmi >= 18.5 and bmi <24.9:
		print("正常")
	elif bmi >= 24.9 and bmi <29.9:
		print("偏胖")
	else:
		print("肥胖")

func_bmi("Amos", 1.80, 84)
func_bmi("Long", 1.68, 54)