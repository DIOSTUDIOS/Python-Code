import re


pattern = r"mr_\w+"
string = "MR_SHOP mr_shop"
match = re.match(pattern, string, re.I)
print(match)

string = "项目名称MR_SHOP mr_shop"
match = re.match(pattern, string, re.I)
print(match)