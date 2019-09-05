class TVshow:
	film_list = ["战狼2", "红海行动", "西游记女儿国", "熊出没", "变形记"]

	def __init__(self, show):
		self.__show = show

	@property
	def show(self):
		return self.__show
	
	@show.setter
	def show(self, value):
		if value in TVshow.film_list:
			self.__show = "你选择了 《" + value + "》，稍后播出！"
		else:
			self.__show = "你点播的电影不存在！"


if __name__ == "__main__":
	tvshow = TVshow("战狼2")
	print(tvshow._TVshow__show)
	print("正在播放：《", tvshow.show, "》")
	print("你可以从", tvshow.film_list, "中选择要点播的电影")

	tvshow.show = "葫芦娃"
	print(tvshow.show)