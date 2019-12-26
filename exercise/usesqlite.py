import sqlite3

# 创建数据表
# conn = sqlite3.connect('mrsoft.db')
# cursor = conn.cursor()
# cursor.execute(r"CREATE TABLE USER(id int(10) primary key, name varchar(20))")
# cursor.close()
# conn.close()

# 向数据表中插入数据
# dblink = sqlite3.connect("mrsoft.db")
# dbcsor = dblink.cursor()

# dbcsor.execute(r"INSERT INTO USER(id, name) VALUES('1', 'MRSoft')")
# dbcsor.execute(r"INSERT INTO USER(id, name) VALUES('2', 'Andy')")
# dbcsor.execute(r"INSERT INTO USER(id, name) VALUES('3', '明日科技小助手')")

# dbcsor.close()
# dblink.commit()
# dblink.close()

# 查询数据表
dblink = sqlite3.connect("mrsoft.db")
dbcsor = dblink.cursor()

dbcsor.execute(r"SELECT * FROM USER")
# result = dbcsor.fetchone()
# print(result)

result = dbcsor.fetchmany(2)
print(result)

# result = dbcsor.fetchall()
# print(result)

dbcsor.close()
dblink.close()