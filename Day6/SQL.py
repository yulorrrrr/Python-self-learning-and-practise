from pymysql import Connection
conn = Connection(
    host='localhost',
    port = 3306,
    user = 'root',
    password="huang060524",
    autocommit= True # or conn.commit after changing
)

cursor = conn.cursor()
#choose database
conn.select_db("sys")
#cursor.execute("create table test_pymysql(id int);")

'''
cursor.execute("select * from student")

result = cursor.fetchall()
print(result)
'''

cursor.execute("insert into student value(4, 'ben', 22)")
#conn.commit()

conn.close()