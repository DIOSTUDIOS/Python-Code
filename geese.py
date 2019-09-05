class Geese:
	def __init__(self, beak, wing, claw):
		print("我是一只大雁，我有以下特征：")
		print(beak)
		print(wing)
		print(claw)

	def fly(self, state):
		print(state)


beak_1 = "嘴的基部较高，长度和头部的长度几乎相等"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是蹼状的"

wildGeese = Geese(beak_1, wing_1, claw_1)
wildGeese.fly("我飞行的时候，一会排成人字，一会排成一字")