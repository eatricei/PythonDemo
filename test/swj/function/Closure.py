# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax+n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
# 每次调用都会返回一个新的函数
# 返回函数不要饮用任何循环变量和后续会发生变化的变量
print((lambda :5*5)()) # 匿名函数