# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(type(now))  # datetime是模块 还包含一个datetime类 导入datetime必须用datetime.datetime

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp 1970年以前的时间timestamp为负数 timestamp = 0 = 1970-1-1 00:00:00 UTC+0.00
# (北京时间timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00) 全球计算机在任意时刻的timestamp都是完全相同的

tt = dt.timestamp()
print(tt)  # python的timestamp是一个浮点数 小数位表示毫秒数
# 某些编程语言(如Java和JavaScript)用整数表示毫秒 只需/1000就是python的毫秒数

t = 1429417200.1234
print(datetime.fromtimestamp(t))  # 采用当前操作系统设置的时区
print(datetime.utcfromtimestamp(t))  # UTC时间

# str转datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)  # 强制转换为UTC+8:00
print(dt)

# 输入两个字符串一个datetime 以及一个时区信息 转换为timestamp
def to_timestamp(dt_str,tz_str):
    return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=(int)(re.match(r'^UTC([+|-][\d]+):(\d{2})$', tz_str).group(1))))).timestamp()

print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00'))