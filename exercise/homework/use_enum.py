from enum import Enum
month=Enum('month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in month.__members__.items():
    print(name,'=>',member,',',member.value)
#value是自动赋给成员的int常量，默认从1开始计数
#要更精确的控制枚举类型，可以从Enum派生出自定义类

from enum import Enum,unique
@unique#帮助检查，保证没有重复值
class weekday(Enum):#类，Enum，不能用objec
    sun=0#sun的value被设定为0
    mon=1
    tue=2
    wed=3
    thu=4
    fri=5
    sat=6

day1=weekday.mon
print(day1)
print(weekday.tue)
print(weekday['wed'])
print(weekday.thu.value)
print(day1==weekday.mon)
print(day1==weekday.tue)
print(weekday(1))
print(day1==weekday(1))
# print(weekday(7))无效越界
for name,member in weekday.__members__.items():
    print(name,'=>',member)