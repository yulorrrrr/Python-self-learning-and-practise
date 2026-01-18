from practice_data_define import *
from practice_file_define import *
import pymysql

text_file_reder = TextFileReader("/Users/huangchuning/Desktop/python/Day5/data01.txt")
json_file_reader = JsonFileReader("/Users/huangchuning/Desktop/python/Day5/data02.txt")

jan_data : list[Record] = text_file_reder.read_data()
feb_data : list[Record] = json_file_reader.read_data()

all_data : list[Record] = jan_data+feb_data


conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="huang060524",
    database="py_sql",   # 直接指定数据库
    autocommit=True
)


cursor = conn.cursor()

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province)" \
          f"values('{record.date}', '{record.order_id}', '{record.money}', '{record.province}')"
    cursor.execute(sql)

conn.close()