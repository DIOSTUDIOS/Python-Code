list = [1, 2, 3, 4, 5]

print(list)

item = list[0]
list[0] = list[3]
list[3] = item

print(list)