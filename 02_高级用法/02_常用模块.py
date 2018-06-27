# calendar
# time
# datetime
# timeeit
# os
# shutil
# zip
# math
# string

import calendar
# w = 每个日期之间的间隔字符数
# l = 每周之间的行数
# c = 每月之间的间隔字符数
cal = calendar.calendar(2018)
print(type(cal))
print(cal)
# isleap 判断某年是否是闰年
print(calendar.isleap(2018))
help(calendar.leapdays)
print(calendar.leapdays(2000, 2018))
calendar.prmonth(2018, 3)
month = calendar.month(2018, 6)
print(month)
weakday = calendar.weekday(2018, 6, 15)
print(weakday)

import  time
# 1970年以前和很久未来很久以后的时间可能会出错
# timezone 当前时区跟UTC时区相差的秒数， 在没有夏令时的情况下
# altzone  当前时区跟UTC时区相差的秒数， 在有夏令时的情况下
# daylight 测当前是否是夏令时时间状态, 0 表示是
print(time.timezone)
print(time.altzone)
print(time.daylight)
# ctime 获取当前时间的字符串
print(time.ctime())
lt = time.localtime()
st = time.mktime(lt)
print(st)
# 格式：time.asctime（时间元组）
# 返回值:字符串 Tue Jun  6 11:11:00 2017
t = time.localtime()
tt = time.asctime(t)
# sleep: 使程序进入睡眠，n秒后继续

for i in range(10):
    print(i)
    time.sleep(1)


def p():
    time.sleep(2.5)

t0 = time.clock()
# p()
time.sleep(3)
t1 = time.clock()

print(t1 - t0)

# strftime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''
# 把时间表示成， 2018年3月26日 21:05
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
print(ft)

import datetime
# datetinme提供日期和时间的运算和表示
# datetime常见属性
# datetime.date: 一个理想和的日期，提供year, month, day属性
dt = datetime.date(2018, 3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time: 提供一个理想和的时间， 居于哦hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度
# datetime.datetime
from datetime import datetime
# 常用类方法：
# today：
# now
# utcnow
# fromtimestamp： 从时间戳中返回本地时间
dt = datetime(2018, 3, 26)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))
# datetime.timedelta
# 表示一个时间间隔

from datetime import datetime, timedelta

t1 = datetime.now()
print( t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print( (t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit-时间测量工具

# 测量程序运行时间间隔实验
def p():
    time.sleep(3.6)


t1 = time.time()
p()
print(time.time() - t1)
