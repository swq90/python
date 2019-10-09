import sqlite3

conn = sqlite3.connect('limit_up.db')
cursor = conn.cursor()
# 建表
# cursor.execute("create table stock_limit (ts_code varchar(10) primary key,"
#                "trade_date varchar(10),close float,pre_close float,change float,pct_chg float)")
# 插入记录
# cursor.execute("insert into stock_limit (ts_code, date, close,pre_close,change,pct_chg) values ")

cursor.execute('select * from stock_limit')
values = cursor.fetchall()
print(values)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭connection
conn.close()