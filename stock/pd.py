import pandas as pd
import numpy as np

ser1 = pd.Series(list("dea990"))
ser2 = pd.Series(list("abcdefg"))
# 水平
print(pd.concat([ser1,ser2], axis=0))

# 垂直
print(pd.concat([ser1,ser2], axis=1))

# series2 = pd.Series([2,2,2,2],['index1','index2','index33','index44'])
# print(series2)
# ser3 = pd.Series(['000892.SZ',20191008,4.25,4.25,0.00,0.0000],['000898.SZ',20191008,3.11,3.09,0.02,0.6472],['000915.SZ',20191008,21.99,21.35,0.64,2.9977],['ts_code','trade_date','close', 'pre_close','change  pct_chg'])
# print(ser3)
# df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# print(df.va)
# print(type(df[['a']]))
# type(df.loc[:, ['a']])
# print(type(df.iloc[:, [0]]))
# print((df.a))
# print(type(df['a']))
# print(type(df.loc[:, 'a']))
# print(type(df.iloc[:, 1]))