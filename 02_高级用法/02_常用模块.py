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