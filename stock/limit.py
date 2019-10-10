import os
import tushare as ts

import numpy as np
import pandas as pd
import datetime

ts.set_token('73bebe31744e1d24de4e95aa59828b2cf9d5e07a40adbbc77a02a53e')
pro = ts.pro_api()
# conn = sqlite3.connect('limit_up.db')
# cursor = conn.cursor()
# 股票信息
# exchange 交易所，list_status 上市状态 L上市 D退市 P暂停，is_hs 是否沪深港通标的，N否 H沪股通 S深股通
stock_basic = pro.stock_basic(exchange='', list_status='', is_hs='',
                       fields='ts_code,symbol,name,area,market,industry,list_date')
#
stock_basic.to_csv('stock_basic.csv')
label = ['ts_code', 'trade_date_x', 'high', 'close', 'pre_close_x', 'change', 'pct_chg', 'trade_date_y', 'pre_close_y', 'up_limit', 'down_limit']
pd.DataFrame(columns=label).to_csv("涨停股票.csv")
pd.DataFrame(columns=label).to_csv('收盘涨停.csv')


days, count = 0, 2

while count:
    end_date = datetime.datetime.today()-datetime.timedelta(days=days)
    date = end_date.strftime('%Y%m%d')
    days += 1
    if pro.query('trade_cal', start_date=date, end_date=date, fields='is_open').values[0][0]:
        count -= 1
    else:
        continue
    # 每日涨跌停价格
    df_limit = pro.stk_limit(trade_date=date, fields='trade_date,ts_code,pre_close,up_limit,down_limit')
    # 每日行情
    df_today = pro.daily(trade_date=date, fields='ts_code,trade_date,pre_close,high,close,change,pct_chg')
    # 将涨停价格列添加到每日行情
    df_up = df_today.merge(df_limit,how='left', on='ts_code')

    # df_up.to_csv('stock_up.csv')
    # 当日涨停股票
    df_up = df_up[df_up['high'] == df_up['up_limit']]
    # 收盘时仍处于涨停的股票
    df_up_end = df_up[df_up['close'] == df_up['up_limit']]
    # if not df_ups:
    #     df_ups = df_up
    # else:
    #     df_ups = pd.concat([df_ups,df_up], axis=0)

    # 打印表头
    # print(list(df_up_end))
    df_up.to_csv("涨停股票.csv", mode='a', header=False)
    df_up_end.to_csv('收盘涨停.csv', mode='a', header=False)
    # print(date+'has done')
    #
    # 某日涨停数量
    print(date, '涨停：', df_up.ts_code.count(), '收盘涨停',df_up_end.ts_code.count())



# df = pro.limit_list(trade_date='20191008')
# print(type(df_limit['ts_code']))
# print(type(df_today['ts_code']))
# df_today[df_today['ts_code'] == df_limit['ts_code']]
# df_up = df_today[df_today['ts_code'] == df_limit['ts_code'] & df_today['close'] >= df_limit['up_limit']]




# for data in df_up.values:
#     print(data)
#     break

# print(df_up.values)

#
# pro.limit_list()
# print(df_up)




# cursor.execute("create table stock_limit (ts_code varchar(10) primary key,"
#                "trade_date varchar(10),close float,pre_close float,change float,pct_chg float)")
# 插入记录
# for data in df_today[6:12]:
#     print(data)
#     # cursor.execute("insert into stock_limit values ('"+data[0]+"','"+data[1]+"','data[2]','data[3]','data[4]','data[5]')")

# cursor.execute('select * from stock_limit')
# values = cursor.fetchall()
# print(values)
# cursor.close()
#
# conn.commit()
#
# conn.close()
#
# # print(data)
# # print(df)
# print(df_today.head())
