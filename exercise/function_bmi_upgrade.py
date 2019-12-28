def fun_bmi_upgrade(*person):
	for list_person in person:
		for item in list_person:
			person = item[0]
			height = item[1]
			weight = item[2]

			print(("=" * 13), person, ("=" * 13))
			print("身高：" + str(height) + "米")
			print("体重：" + str(weight) + "千克")
			bmi = weight/height**2
			print("BMI :" + str(bmi))

			if bmi < 18.5:
				print("过轻")

			if bmi>= 18.5 and bmi < 24.9:
				print("正常")

			if bmi >= 24.9 and nmi < 29.9:
				print("过胖")

			if bmi >= 29.9:
				print("肥胖")


	pass


if __name__ == "__main__":
	list_w = [("绮梦", 1.70, 65), ("玲玉", 1.78, 50), ("黛蓝", 1.72, 66)]
	list_m = [("紫萱", 1.80, 75), ("刘峰", 1.75, 70)]

	fun_bmi_upgrade(list_w, list_m)