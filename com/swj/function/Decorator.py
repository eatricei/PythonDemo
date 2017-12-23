# -*- coding: utf-8 -*-
# 装饰器 函数对象有__name__属性，拿到函数的名字 假设我们要增强函数的功能 有不希望修改函数的定义
# 这种在代码运行期间动态增加功能的方式 称为Decorator 本质上是一个返回函数的高阶函数
# def log(func):  # log就是一个装饰器
#     def wrapper(*args, **kw):  # 可以接受任意参数的调用
#         print('call %s():'% func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log  # 相当于 now = log(now)
# def now():
#     print('2015-3-25')
# now()

# 如果decorator本身就需要参数的传入 比如日志的文本
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)  # 确保原始属性不被改变
        def wrapper(*args, **kw):
            print('%s %s():'%(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')  # 相当于now = log('execute')(now)
def now():
    print('2015-3-25')

now()
print(now.__name__)  # 从now变成了wrapper 需要把原始函数的属性赋值到wrapper函数中 需要functools.wraps