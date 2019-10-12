import tushare as ts
import numpy as np
import pandas as pd
import datetime

ts.set_token('73bebe31744e1d24de4e95aa59828b2cf9d5e07a40adbbc77a02a53e')
pro = ts.pro_api()
# end_date = datetime.datetime.today()-datetime.timedelta(days=0)
# date = end_date.strftime('%Y%m%d')
# # pro.trade_cal(exchange='',start_day='20190920', end_date='20190925')
# print(pro.query('trade_cal', start_date='20191005', end_date='20191005',fields='is_open').values[0][0])

df_limit = pro.stk_limit(trade_date='20191009', fields='trade_date,ts_code,pre_close,up_limit,down_limit')
df_limit.to_csv('updown.csv')
print(df_limit)