# 基础数据
## 股票列表
接口：stock_basic
描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
输入参数
名称	类型	必选	描述
is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
list_status	str	N	上市状态： L上市 D退市 P暂上市
exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)

输出参数

名称	类型	描述
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
area	str	所在地域
industry	str	所属行业
fullname	str	股票全称
enname	str	英文全称
market	str	市场类型 （主板/中小板/创业板/科创板）
exchange	str	交易所代码
curr_type	str	交易货币
list_status	str	上市状态： L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通

## 交易日历
接口：trade_cal
描述：获取各大交易所交易日历数据,默认提取的是上交所

输入参数

名称	类型	必选	描述
exchange	str	N	交易所 SSE上交所 SZSE深交所
start_date	str	N	开始日期
end_date	str	N	结束日期
is_open	str	N	是否交易 '0'休市 '1'交易
输出参数

名称	类型	默认显示	描述
exchange	str	Y	交易所 SSE上交所 SZSE深交所
cal_date	str	Y	日历日期
is_open	str	Y	是否交易 0休市 1交易
pretrade_date	str	N	上一个交易日

## 股票曾用名
接口：namechange
描述：历史名称变更记录

输入参数

名称	类型	必选	描述
ts_code	str	N	TS代码
start_date	str	N	公告开始日期
end_date	str	N	公告结束日期
输出参数

名称	类型	默认输出	描述
ts_code	str	Y	TS代码
name	str	Y	证券名称
start_date	str	Y	开始日期
end_date	str	Y	结束日期
ann_date	str	Y	公告日期
change_reason	str	Y	变更原因


沪深股通成份股
接口：hs_const
描述：获取沪股通、深股通成分数据

输入参数

名称	类型	必选	描述
hs_type	str	Y	类型SH沪股通SZ深股通
is_new	str	N	是否最新 1 是 0 否 (默认1)


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS代码
hs_type	str	Y	沪深港通类型SH沪SZ深
in_date	str	Y	纳入日期
out_date	str	Y	剔除日期
is_new	str	Y	是否最新 1是 0否

## 沪深股通成份股
接口：hs_const
描述：获取沪股通、深股通成分数据

输入参数

名称	类型	必选	描述
hs_type	str	Y	类型SH沪股通SZ深股通
is_new	str	N	是否最新 1 是 0 否 (默认1)


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS代码
hs_type	str	Y	沪深港通类型SH沪SZ深
in_date	str	Y	纳入日期
out_date	str	Y	剔除日期
is_new	str	Y	是否最新 1是 0否

## 上市公司基本信息
接口：stock_company
描述：获取上市公司基础信息
积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法

输入参数

名称	类型	默认显示	描述
exchange	str	N	交易所代码 ，SSE上交所 SZSE深交所 ，默认SSE
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	股票代码
exchange	str	Y	交易所代码 ，SSE上交所 SZSE深交所
chairman	str	Y	法人代表
manager	str	Y	总经理
secretary	str	Y	董秘
reg_capital	float	Y	注册资本
setup_date	str	Y	注册日期
province	str	Y	所在省份
city	str	Y	所在城市
introduction	str	N	公司介绍
website	str	Y	公司主页
email	str	Y	电子邮件
office	str	N	办公室
employees	int	Y	员工人数
main_business	str	N	主要业务及产品
business_scope	str	N	经营范围

## 上市公司管理层
接口：stk_managers
描述：获取上市公司管理层
积分：用户需要2000积分才可以调取，5000积分以上无限制，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
ts_code	str	Y	股票代码，支持单个或多个股票输入


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS股票代码
ann_date	str	Y	公告日期
name	str	Y	姓名
gender	str	Y	性别
lev	str	Y	岗位类别
title	str	Y	岗位
edu	str	Y	学历
national	str	Y	国籍
birthday	str	Y	出生年月
begin_date	str	Y	上任日期
end_date	str	Y	离任日期
resume	str	N	个人简历

## 管理层薪酬和持股
接口：stk_rewards
描述：获取上市公司管理层薪酬和持股
积分：用户需要2000积分才可以调取，5000积分以上无限制，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
ts_code	str	Y	TS股票代码，支持单个或多个代码输入
end_date	str	N	报告期


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS股票代码
ann_date	str	Y	公告日期
end_date	str	Y	截止日期
name	str	Y	姓名
title	str	Y	职务
reward	float	Y	报酬
hold_vol	float	Y	持股数

## IPO新股列表
接口：new_share
描述：获取新股上市列表数据
限量：单次最大2000条，总量不限制
积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法

输入参数

名称	类型	必选	描述
start_date	str	N	上网发行开始日期
end_date	str	N	上网发行结束日期
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS股票代码
sub_code	str	Y	申购代码
name	str	Y	名称
ipo_date	str	Y	上网发行日期
issue_date	str	Y	上市日期
amount	float	Y	发行总量（万股）
market_amount	float	Y	上网发行总量（万股）
price	float	Y	发行价格
pe	float	Y	市盈率
limit_amount	float	Y	个人申购上限（万股）
funds	float	Y	募集资金（亿元）
ballot	float	Y	中签率

# 行情数据
## 日线行情
接口：daily
数据说明：交易日每天15点～16点之间。本接口是未复权行情，停牌期间不提供数据。
调取说明：基础积分每分钟内最多调取200次，每次4000条数据，相当于超过18年历史，用户获得超过5000积分无频次限制。
描述：获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据。

输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码（二选一）
trade_date	str	N	交易日期（二选一）
start_date	str	N	开始日期(YYYYMMDD)
end_date	str	N	结束日期(YYYYMMDD)
注：日期都填YYYYMMDD格式，比如20181010

输出参数

名称	类型	描述
ts_code	str	股票代码
trade_date	str	交易日期
open	float	开盘价
high	float	最高价
low	float	最低价
close	float	收盘价
pre_close	float	昨收价
change	float	涨跌额
pct_chg	float	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
vol	float	成交量 （手）
amount	float	成交额 （千元）

## 周线行情
接口：weekly
描述：获取A股周线行情
限量：单次最大3700，总量不限制
积分：用户需要至少300积分才可以调取，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
ts_code	str	N	TS代码 （ts_code,trade_date两个参数任选一）
trade_date	str	N	交易日期 （每周五日期，YYYYMMDD格式）
start_date	str	N	开始日期
end_date	str	N	结束日期


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	股票代码
trade_date	str	Y	交易日期
close	float	Y	周收盘价
open	float	Y	周开盘价
high	float	Y	周最高价
low	float	Y	周最低价
pre_close	float	Y	上一周收盘价
change	float	Y	周涨跌额
pct_chg	float	Y	周涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
vol	float	Y	周成交量
amount	float	Y	周成交额

## 月线行情
接口：monthly
描述：获取A股月线数据
限量：单次最大3700，总量不限制
积分：用户需要至少300积分才可以调取，具体请参阅积分获取办法

输入参数

名称	类型	必选	描述
ts_code	str	N	TS代码 （ts_code,trade_date两个参数任选一）
trade_date	str	N	交易日期 （每月最后一个交易日日期，YYYYMMDD格式）
start_date	str	N	开始日期
end_date	str	N	结束日期
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	股票代码
trade_date	str	Y	交易日期
close	float	Y	月收盘价
open	float	Y	月开盘价
high	float	Y	月最高价
low	float	Y	月最低价
pre_close	float	Y	上月收盘价
change	float	Y	月涨跌额
pct_chg	float	Y	月涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
vol	float	Y	月成交量
amount	float	Y	月成交额

## A股复权行情
接口名称 ：pro_bar
接口说明 ：复权行情通过通用行情接口实现，利用Tushare Pro提供的复权因子进行计算，目前暂时只在SDK中提供支持，http方式无法调取。
Python SDK版本要求： >= 1.2.26



复权说明

类型	算法	参数标识
不复权	无	空或None
前复权	当日收盘价 × 当日复权因子 / 最新复权因子	qfq
后复权	当日收盘价 × 当日复权因子	hfq
注：目前支持A股的日线/周线/月线复权，分钟复权稍后支持



接口参数

名称	类型	必选	描述
ts_code	str	Y	证券代码
pro_api	str	N	pro版api对象
start_date	str	N	开始日期 (格式：YYYYMMDD)
end_date	str	N	结束日期 (格式：YYYYMMDD)
asset	str	Y	资产类别：E股票 I沪深指数 C数字货币 F期货 FD基金 O期权，默认E
adj	str	N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
freq	str	Y	数据频度 ：1MIN表示1分钟（1/5/15/30/60分钟） D日线 ，默认D
ma	list	N	均线，支持任意周期的均价和均量，输入任意合理int数值

## 复权因子
接口：adj_factor
更新时间：早上9点30分
描述：获取股票复权因子，可提取单只股票全部历史复权因子，也可以提取单日全部股票的复权因子。

输入参数

名称	类型	必选	描述
ts_code	str	Y	股票代码
trade_date	str	N	交易日期(YYYYMMDD，下同)
start_date	str	N	开始日期
end_date	str	N	结束日期
注：日期都填YYYYMMDD格式，比如20181010

输出参数

名称	类型	描述
ts_code	str	股票代码
trade_date	str	交易日期
adj_factor	float	复权因子

## 停复牌信息
接口：suspend
更新时间：不定期
描述：获取股票每日停复牌信息

输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码(三选一)
suspend_date	str	N	停牌日期(三选一)
resume_date	str	N	复牌日期(三选一)
输出参数

名称	类型	描述
ts_code	str	股票代码
suspend_date	str	停牌日期
resume_date	str	复牌日期
ann_date	str	公告日期
suspend_reason	str	停牌原因
reason_type	str	停牌原因类别

## 每日指标
接口：daily_basic
更新时间：交易日每日15点～17点之间
描述：获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。
积分：用户需要至少300积分才可以调取，具体请参阅积分获取办法

输入参数

名称	类型	必选	描述
ts_code	str	Y	股票代码（二选一）
trade_date	str	N	交易日期 （二选一）
start_date	str	N	开始日期(YYYYMMDD)
end_date	str	N	结束日期(YYYYMMDD)
注：日期都填YYYYMMDD格式，比如20181010

输出参数

名称	类型	描述
ts_code	str	TS股票代码
trade_date	str	交易日期
close	float	当日收盘价
turnover_rate	float	换手率（%）
turnover_rate_f	float	换手率（自由流通股）
volume_ratio	float	量比
pe	float	市盈率（总市值/净利润）
pe_ttm	float	市盈率（TTM）
pb	float	市净率（总市值/净资产）
ps	float	市销率
ps_ttm	float	市销率（TTM）
total_share	float	总股本 （万股）
float_share	float	流通股本 （万股）
free_share	float	自由流通股本 （万）
total_mv	float	总市值 （万元）
circ_mv	float	流通市值（万元）
## 通用行情接口
接口名称：pro_bar
更新时间：股票和指数通常在15点～17点之间，数字货币实时更新，具体请参考各接口文档明细。
描述：目前整合了股票（未复权、前复权、后复权）、指数、数字货币、ETF基金、期货、期权的行情数据，未来还将整合包括外汇在内的所有交易行情数据，同时提供分钟数据。
其它：由于本接口是集成接口，在SDK层做了一些逻辑处理，目前暂时没法用http的方式调取通用行情接口。用户可以访问Tushare的Github，查看源代码完成类似功能。

输入参数

名称	类型	必选	描述
ts_code	str	Y	证券代码
api	str	N	pro版api对象，如果初始化了set_token，此参数可以不需要
start_date	str	N	开始日期 (格式：YYYYMMDD)
end_date	str	N	结束日期 (格式：YYYYMMDD)
asset	str	Y	资产类别：E股票 I沪深指数 C数字货币 FT期货 FD基金 O期权 CB可转债（v1.2.39），默认E
adj	str	N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
freq	str	Y	数据频度 ：支持分钟(min)/日(D)/周(W)/月(M)K线，其中1min表示1分钟（类推1/5/15/30/60分钟） ，默认D。目前有120积分的用户自动具备分钟数据试用权限（每分钟5次），正式权限请在QQ群私信群主。
ma	list	N	均线，支持任意合理int数值
factors	list	N	股票因子（asset='E'有效）支持 tor换手率 vr量比
adjfactor	str	N	复权因子，在复权数据是，如果此参数为True，返回的数据中则带复权因子，默认为False。 该功能从1.2.33版本开始生效

## 个股资金流向
接口：moneyflow
描述：获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向
限量：单次最大提取4000行记录，总量不限制
积分：用户需要至少1500积分才可以调取，基础积分有流量控制，积分越多权限越大，请自行提高积分，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码 （股票和时间参数至少输入一个）
trade_date	str	N	交易日期
start_date	str	N	开始日期
end_date	str	N	结束日期


输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS代码
trade_date	str	Y	交易日期
buy_sm_vol	int	Y	小单买入量（手）
buy_sm_amount	float	Y	小单买入金额（万元）
sell_sm_vol	int	Y	小单卖出量（手）
sell_sm_amount	float	Y	小单卖出金额（万元）
buy_md_vol	int	Y	中单买入量（手）
buy_md_amount	float	Y	中单买入金额（万元）
sell_md_vol	int	Y	中单卖出量（手）
sell_md_amount	float	Y	中单卖出金额（万元）
buy_lg_vol	int	Y	大单买入量（手）
buy_lg_amount	float	Y	大单买入金额（万元）
sell_lg_vol	int	Y	大单卖出量（手）
sell_lg_amount	float	Y	大单卖出金额（万元）
buy_elg_vol	int	Y	特大单买入量（手）
buy_elg_amount	float	Y	特大单买入金额（万元）
sell_elg_vol	int	Y	特大单卖出量（手）
sell_elg_amount	float	Y	特大单卖出金额（万元）
net_mf_vol	int	Y	净流入量（手）
net_mf_amount	float	Y	净流入额（万元）

各类别统计规则如下：
小单：5万以下 中单：5万～20万 大单：20万～100万 特大单：成交额>=100万
## 每日涨跌停价格
接口：stk_limit
描述：获取全市场（包含A/B股和基金）每日涨跌停价格，包括涨停价格，跌停价格等，每个交易日8点40左右更新当日股票涨跌停价格。
限量：单次最多提取4800条记录，可循环调取，总量不限制
积分：用户积600积分可调取，单位分钟有流控，积分越高流量越大，请自行提高积分，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码
trade_date	str	N	交易日期
start_date	str	N	开始日期
end_date	str	N	结束日期


输出参数

名称	类型	默认显示	描述
trade_date	str	Y	交易日期
ts_code	str	Y	TS股票代码
pre_close	float	N	昨日收盘价
up_limit	float	Y	涨停价
down_limit	float	Y	跌停价
## 每日涨跌停统计
接口：limit_list
描述：获取每日涨跌停股票统计，包括封闭时间和打开次数等数据，帮助用户快速定位近期强（弱）势股，以及研究超短线策略。
限量：单次最大1000，总量不限制
积分：用户积2000积分可调取，5000积分以上可高频使用，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
trade_date	str	N	交易日期 YYYYMMDD格式，支持单个或多日期输入
ts_code	str	N	股票代码 （支持单个或多个股票输入）
limit_type	str	N	涨跌停类型：U涨停D跌停
start_date	str	N	开始日期 YYYYMMDD格式
end_date	str	N	结束日期 YYYYMMDD格式


输出参数

名称	类型	默认显示	描述
trade_date	str	Y	交易日期
ts_code	str	Y	股票代码
name	str	Y	股票名称
close	float	Y	收盘价
pct_chg	float	Y	涨跌幅
amp	float	Y	振幅
fc_ratio	float	Y	封单金额/日成交金额
fl_ratio	float	Y	封单手数/流通股本
fd_amount	float	Y	封单金额
first_time	str	Y	首次涨停时间
last_time	str	Y	最后封板时间
open_times	int	Y	打开次数
strth	float	Y	涨跌停强度
limit	str	Y	D跌停U涨停

## 沪深港通资金流向
接口：moneyflow_hsgt
描述：获取沪股通、深股通、港股通每日资金流向数据，每次最多返回300条记录，总量不限制。

输入参数

名称	类型	必选	描述
trade_date	str	N	交易日期 (二选一)
start_date	str	N	开始日期 (二选一)
end_date	str	N	结束日期
输出参数

名称	类型	描述
trade_date	str	交易日期
ggt_ss	float	港股通（上海）
ggt_sz	float	港股通（深圳）
hgt	float	沪股通（百万元）
sgt	float	深股通（百万元）
north_money	float	北向资金（百万元）
south_money	float	南向资金（百万元）

## 沪深股通十大成交股
接口：hsgt_top10
描述：获取沪股通、深股通每日前十大成交详细数据

输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码（二选一）
trade_date	str	N	交易日期（二选一）
start_date	str	N	开始日期
end_date	str	N	结束日期
market_type	str	N	市场类型（1：沪市 3：深市）
输出参数

名称	类型	描述
trade_date	str	交易日期
ts_code	str	股票代码
name	str	股票名称
close	float	收盘价
change	float	涨跌额
rank	int	资金排名
market_type	str	市场类型（1：沪市 3：深市）
amount	float	成交金额（元）
net_amount	float	净成交金额（元）
buy	float	买入金额（元）
sell	float	卖出金额（元）

## 沪深港股通持股明细
接口：hk_hold
描述：获取沪深港股通持股明细，数据来源港交所。
限量：单次最多提取3800条记录，可循环调取，总量不限制
积分：用户积120积分可调取试用，2000积分可正常使用，单位分钟有流控，积分越高流量越大，请自行提高积分，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
code	str	N	交易所代码
ts_code	str	N	TS股票代码
trade_date	str	N	交易日期
start_date	str	N	开始日期
end_date	str	N	结束日期
exchange	str	N	类型：SH沪股通（北向）SZ深股通（北向）HK港股通（南向持股）


输出参数

名称	类型	默认显示	描述
code	str	Y	原始代码
trade_date	str	Y	交易日期
ts_code	str	Y	TS代码
name	str	Y	股票名称
vol	int	Y	持股数量(股)
ratio	float	Y	持股占比（%）
exchange	str	Y	类型：SH沪股通SZ深港通HK港股通

## 港股通每日成交统计
接口：ggt_daily
描述：获取港股通每日成交信息，数据从2014年开始
限量：单次最大1000，总量数据不限制
积分：用户积2000积分可调取，5000积分无限制，请自行提高积分，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
trade_date	str	N	交易日期 （格式YYYYMMDD，下同。支持单日和多日输入）
start_date	str	N	开始日期
end_date	str	N	结束日期


输出参数

名称	类型	默认显示	描述
trade_date	str	Y	交易日期
buy_amount	float	Y	买入成交金额（亿元）
buy_volume	float	Y	买入成交笔数（万笔）
sell_amount	float	Y	卖出成交金额（亿元）
sell_volume	float	Y	卖出成交笔数（万笔）

## 港股通每月成交统计
接口：ggt_monthly
描述：港股通每月成交信息，数据从2014年开始
限量：单次最大1000
积分：用户积5000积分可调取，请自行提高积分，具体请参阅积分获取办法



输入参数

名称	类型	必选	描述
month	str	N	月度（格式YYYYMM，下同，支持多个输入）
start_month	str	N	开始月度
end_month	str	N	结束月度


输出参数

名称	类型	默认显示	描述
month	str	Y	交易日期
day_buy_amt	float	Y	当月日均买入成交金额（亿元）
day_buy_vol	float	Y	当月日均买入成交笔数（万笔）
day_sell_amt	float	Y	当月日均卖出成交金额（亿元）
day_sell_vol	float	Y	当月日均卖出成交笔数（万笔）
total_buy_amt	float	Y	总买入成交金额（亿元）
total_buy_vol	float	Y	总买入成交笔数（万笔）
total_sell_amt	float	Y	总卖出成交金额（亿元）
total_sell_vol	float	Y	总卖出成交笔数（万笔）

# 财务数据
Pro版的财务数据跟旧版有着明显的差异，Pro提供的是完整的财务指标和全部历史数据，同时也提供质量比较高的业绩预告和业绩快报数据。我们将继续完善和充实财务指标，为大家提供更全面的反映上市公司基本面情况的数据，希望大家愉快的使用。

## 利润表
接口：income
描述：获取上市公司财务利润表数据
积分：用户需要至少500积分才可以调取，具体请参阅积分获取办法

提示：当前接口只能按单只股票获取其历史数据，如果需要获取某一季度全部上市公司数据，请使用income_vip接口（参数一致），需积攒5000积分。

输入参数

名称	类型	必选	描述
ts_code	str	Y	股票代码
ann_date	str	N	公告日期
start_date	str	N	公告开始日期
end_date	str	N	公告结束日期
period	str	N	报告期(每个季度最后一天的日期，比如20171231表示年报)
report_type	str	N	报告类型： 参考下表说明
comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS代码
ann_date	str	Y	公告日期
f_ann_date	str	Y	实际公告日期
end_date	str	Y	报告期
report_type	str	Y	报告类型 1合并报表 2单季合并 3调整单季合并表 4调整合并报表 5调整前合并报表 6母公司报表 7母公司单季表 8 母公司调整单季表 9母公司调整表 10母公司调整前报表 11调整前合并报表 12母公司调整前报表
comp_type	str	Y	公司类型(1一般工商业2银行3保险4证券)
basic_eps	float	Y	基本每股收益
diluted_eps	float	Y	稀释每股收益
total_revenue	float	Y	营业总收入
revenue	float	Y	营业收入
int_income	float	Y	利息收入
prem_earned	float	Y	已赚保费
comm_income	float	Y	手续费及佣金收入
n_commis_income	float	Y	手续费及佣金净收入
n_oth_income	float	Y	其他经营净收益
n_oth_b_income	float	Y	加:其他业务净收益
prem_income	float	Y	保险业务收入
out_prem	float	Y	减:分出保费
une_prem_reser	float	Y	提取未到期责任准备金
reins_income	float	Y	其中:分保费收入
n_sec_tb_income	float	Y	代理买卖证券业务净收入
n_sec_uw_income	float	Y	证券承销业务净收入
n_asset_mg_income	float	Y	受托客户资产管理业务净收入
oth_b_income	float	Y	其他业务收入
fv_value_chg_gain	float	Y	加:公允价值变动净收益
invest_income	float	Y	加:投资净收益
ass_invest_income	float	Y	其中:对联营企业和合营企业的投资收益
forex_gain	float	Y	加:汇兑净收益
total_cogs	float	Y	营业总成本
oper_cost	float	Y	减:营业成本
int_exp	float	Y	减:利息支出
comm_exp	float	Y	减:手续费及佣金支出
biz_tax_surchg	float	Y	减:营业税金及附加
sell_exp	float	Y	减:销售费用
admin_exp	float	Y	减:管理费用
fin_exp	float	Y	减:财务费用
assets_impair_loss	float	Y	减:资产减值损失
prem_refund	float	Y	退保金
compens_payout	float	Y	赔付总支出
reser_insur_liab	float	Y	提取保险责任准备金
div_payt	float	Y	保户红利支出
reins_exp	float	Y	分保费用
oper_exp	float	Y	营业支出
compens_payout_refu	float	Y	减:摊回赔付支出
insur_reser_refu	float	Y	减:摊回保险责任准备金
reins_cost_refund	float	Y	减:摊回分保费用
other_bus_cost	float	Y	其他业务成本
operate_profit	float	Y	营业利润
non_oper_income	float	Y	加:营业外收入
non_oper_exp	float	Y	减:营业外支出
nca_disploss	float	Y	其中:减:非流动资产处置净损失
total_profit	float	Y	利润总额
income_tax	float	Y	所得税费用
n_income	float	Y	净利润(含少数股东损益)
n_income_attr_p	float	Y	净利润(不含少数股东损益)
minority_gain	float	Y	少数股东损益
oth_compr_income	float	Y	其他综合收益
t_compr_income	float	Y	综合收益总额
compr_inc_attr_p	float	Y	归属于母公司(或股东)的综合收益总额
compr_inc_attr_m_s	float	Y	归属于少数股东的综合收益总额
ebit	float	Y	息税前利润
ebitda	float	Y	息税折旧摊销前利润
insurance_exp	float	Y	保险业务支出
undist_profit	float	Y	年初未分配利润
distable_profit	float	Y	可分配利润
update_flag	str	N	更新标识，0未修改1更正过
主要报表类型说明

代码	类型	说明
1	合并报表	上市公司最新报表（默认）
2	单季合并	单一季度的合并报表
3	调整单季合并表	调整后的单季合并报表（如果有）
4	调整合并报表	本年度公布上年同期的财务报表数据，报告期为上年度
5	调整前合并报表	数据发生变更，将原数据进行保留，即调整前的原数据
6	母公司报表	该公司母公司的财务报表数据
7	母公司单季表	母公司的单季度表
8	母公司调整单季表	母公司调整后的单季表
9	母公司调整表	该公司母公司的本年度公布上年同期的财务报表数据
10	母公司调整前报表	母公司调整之前的原始财务报表数据
11	调整前合并报表	调整之前合并报表原数据
12	母公司调整前报表	母公司报表发生变更前保留的原数据

## 

## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
# 市场参考数据
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## ## 
## 
## 
## # 
# 指数
# 基金
# 期货
# 期权
# 债券
# 
# # 
# 外汇
# 
# 港股
# # 
# 行业经济
# 
# 
# # 
# 宏观经济
# 
# 特色大数据
# # 
# 
# 
# 
# 
# 
# 
# 
# 
# 