template = "编号：{:0<9s}\t公司名称：{:s}\t官网：http://www.{:s}.com"

str1 = template.format("7", "百度", "baidu")
str2 = template.format("8", "明日科技", "mingrisoft")

print(str1)
print(str2)
