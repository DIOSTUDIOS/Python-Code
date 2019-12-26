import pymongo


mg_linker = pymongo.MongoClient(host='localhost', port=27017)
mg_databs = mg_linker['student_information']
mg_gather = mg_databs['report']
# 插入一行数据
# datum = {"name": "Amos", "Chinese": 97, "Math": 100, "English": 95}
# mg_gather.insert_one(datum)

# 插入多行数据
# data = [
# 	{"name": "Lucy",   "Chinese": 99, "Math": 95,  "English": 90},
# 	{"name": "Lily",   "Chinese": 87, "Math": 58,  "English": 59},
# 	{"name": "James",  "Chinese": 58, "Math": 20,  "English": 26},
# 	{"name": "Jack",   "Chinese": 60, "Math": 78,  "English": 32},
# 	{"name": "Thomas", "Chinese": 42, "Math": 100, "English": 99},
# ]
# mg_gather.insert_many(data)

# 删除一行数据
# mg_gather.delete_one({"name": "Amos"})

# 删除所有符合条件的数据
# mg_gather.delete_many({"name": "Amos"})

# result = mg_gather.find_one({"name": "Amos"})
# print(result)

# result = mg_gather.find({"name": "Amos"})

# result = mg_gather.find({"Math": {"$gt": 90}})
# result = mg_gather.find({"Math": {"$gte": 90}})
# result = mg_gather.find({"Math": {"$lt": 90}})
# result = mg_gather.find({"Math": {"$lte": 90}})

# result = mg_gather.find({"name": {"$regex": "os$"}})
# result = mg_gather.find().limit(3)

# mg_gather.find().count()

# for item in result:
# 	print(item)

# mg_gather.update_many({"name": "Amos"}, {"$set": {"Math": 0}})
results = mg_gather.find().sort("name", -1).skip(1)

for item in results:
	print(item["name"])