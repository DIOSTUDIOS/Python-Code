def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	assert apple > child, "苹果不够分。"

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
	except ValueError as e:
		print("输入错误！！！", e)
	else:
		print("苹果分配成功。。。")
	finally:
		print("分配了一次苹果。")