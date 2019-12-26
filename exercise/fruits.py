class Fruit:
	def __init__(self, color = "green"):
		Fruit.color = color

	def harvest(self, color):
		print("水果是：" + self.color + "的！")
		print("水果已经收获...")
		print("水果原来是：" + Fruit.color + "的！")


class Apple(Fruit):
	color = "red"

	def __init__(self):
		print("I am an apple")
		super().__init__()


class Sapodilla(Fruit):
	def __init__(self, color):
		print("I am a sapodilla")
		super().__init__(color)

	def harvest(self, color):
		print("人参果是：" + color + "的！")
		print("人参果已经收获...")
		print("人参果原来是：" + Fruit.color + "的！")


if __name__ == "__main__":
	apple = Apple()
	apple.harvest(apple.color)

	sapodilla = Sapodilla("white")
	sapodilla.harvest("金黄色带紫色条纹")
