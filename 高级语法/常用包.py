# -*- coding: utf-8 -*-
import calendar#日历
import time
from datetime import datetime#时间和日期的运算和表示
import timeit#测量一个函数的执行时间
cal = calendar.calendar(2018)
print(cal)

#isleap：判断是否闰年
#leapdays：判断指定年份之间闰年个数


#timezone:当前系统的时区和UTC时间相差的秒数

t = time.ctime()#当前时间
print(t)

#strftime 将时间元祖格式化为自定义格式
t = time.localtime()
ft = time.strftime("%Yyear%mmonth%dday %H:%M",t)
print(ft)


print(datetime.now())


