import pandas as pd

#股票信息
stock_basic = pd.read_csv('stock_basic.csv')
# 读取涨停数据
df_up_end = pd.read_csv('收盘涨停.csv')
uplist = df_up_end.groupby(by='ts_code').count().reset_index()
# uplist = df_up_end
print(list(uplist)      )
uplist.rename(columns={'Unnamed: 0': 'count'})
print(uplist)
# 表中股票几日内出现的涨停次数
# freq = df_up_end['ts_code'].value_counts()
# print(list(df_up_end))




# 统计周期内股票涨停次数
freq2 = df_up_end.groupby(by='ts_code')['close'].count()
# print(freq, freq2,df_up_end[1:2]['up_limit'])
print(freq2)

# 涨停股票信息
# up_info = stock_basic[stock_basic['ts_code'] == uplist['ts_code'].squeeze()]
up_info = stock_basic.loc[stock_basic["ts_code"] in uplist].head
#
# up_info = pd.merge(left=df_up_end, right=stock_basic,on='ts_code')
print(up_info)


# print(up_info)
# print(stock_basic['ts_code'])
# freq_info = freq.merge(stock_basic,how='left',left_on = 'index',right_on='ts_code')
#
# print(freq_info)