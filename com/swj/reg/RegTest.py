# -*- coding: utf-8 -*-
import re

s = 'ABC\\-001'  # python 中的字符串 对应的正则表达式变成'ABC\-001'

s = r'ABC\-001'  # 加上r前缀就不用考虑转义的问题了

re.match(r'^\d{3}\-\d{3,8}$','010-12345')  # 匹配成功返回Match对象,否则返回None
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

re.split(r'\s+','a b   c')
re.split(r'[\s\,\;]+','a,b, ;;c')

# 分组 ( ) group(0)永远为原字符串
m = re.match(r'^(\d{3})-(\d{3,8}$)', '010-12345')
print(m)
print(m.group(0))

# 贪婪匹配(默认) -- 尽可能多得去匹配
re.match(r'^(\d+)(0*)$','102300').groups()  # ('102300', '')
# 加? 采用非贪婪匹配
re.match(r'^(\d+?)(0*)$','102300').groups()  # ('1023', '00')

# 编译 如果一个正则表达式要被使用很多次 我们可以预编译来提升效率

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('101-12345').groups()
re_telephone.match('123-456').groups()


