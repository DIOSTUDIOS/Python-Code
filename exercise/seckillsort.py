bookinfo = [
			("不一样的卡梅拉", 22.50, 120.00),
			("零基础学Python", 65.10, 80.00),
			("摆渡人", 23.40, 36.00),
			("福尔摩斯探案", 22.50, 128.00)
		]

bookinfo.sort(key = lambda x:(x[1], x[1]/x[2]))

print(bookinfo)