from datetime import datetime
import time as _time
now=datetime.now()
print(now)
print(type(now))
dt=datetime(2019,5,20,13,14)#有时区
print(dt)
#timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
#把datetime类型转换为timestamp，用timestamp（）
ts=dt.timestamp()#标准无时区概念，会根据系统时间转换
print(ts)#浮点数，小数位表示浮点数
#timestamp转换为datetime
fts=datetime.fromtimestamp(ts)
fts1=datetime.utcfromtimestamp(ts)#utc时间
print('a',fts)
print(fts1)
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')#规定了时间和日期的格式
print(cday)#2015-06-01 18:19:59
#将字符串格式化为时间，转换后的datetime是没有时区的

#datetime转换为str
print(now.strftime('%a,%b %d %H:%M'))#Tue,May 14 20:32

#datetime加减
from datetime import datetime,timedelta
print(now+timedelta(hours=10))
print('+1week',now-timedelta(weeks=1))
print(now+timedelta(days=1,seconds=30))

#一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
from datetime import  datetime ,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=9)) # 创建时区UTC+8:00
now = datetime.now()
print('b',now)#2019-05-16 10:09:33.159384
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00(系统时间为utc+8才可以?可以啊
print(dt)# 2019-05-16 10:09:33.159384+08:00

#时区转换
utc_dt=datetime.utcnow()#得到utc时间
print(utc_dt)
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)#先打到utc，在强制时区为utc 0(可以强制么？）
#astimezone()转换为北京时区
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print('pk',bj_dt)
#astimezone()转换为东京时区
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo',tokyo_dt)
#astimezone()北京时区转换为东京时区
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo2',tokyo_dt2)
#datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关