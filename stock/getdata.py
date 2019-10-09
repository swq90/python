import tushare as ts
import numpy as np

ts.set_token('73bebe31744e1d24de4e95aa59828b2cf9d5e07a40adbbc77a02a53e')
pro = ts.pro_api()

# df = pro.trade_cal(exchange='', start_date='20190901', end_date='20191001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# df = pro.query('trade_cal', exchange='', start_date='20190901', end_date='20191001',
#                fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
df_today = pro.daily(trade_date='20191008', fields='ts_code,trade_date,pre_close,close,change,pct_chg')


# print(df_today)
for i in df_today:
    print(i[11])