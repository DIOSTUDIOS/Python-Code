class Fruit:
	color = "green"

	def harvest(self, color):
		print("fruit`s color is " + color)
		print("水果已经收获....")
		print("水果原来是" + Fruit.color + "的！")


class Apple(Fruit):
	color = "red"

	def __init__(self):
		print("I am an apple")


class Orange(Fruit):
	color = "orange"

	def __init__(self):
		print("I am an orange")


if __name__ == "__main__":
	apple = Apple()
	apple.harvest(apple.color)

	orange = Orange()
	orange.harvest(orange.color)