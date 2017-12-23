# -*- coding: utf-8 -*-
def power(x):  # 必选参数
    return x*x

def power2(x, n=3):  # 默认参数 必须指向不可变对象
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def calc(* numbers):  # 可变参数 允许传入任意个参数 自动接收为tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

def person(name, age, **kw):  # 关键字参数 允许传入任意个含参数名的参数 自动接收为dict
    print('name:',name,' age:',age,' other',kw)

def person2(name, age, *, job, city):  # 命名关键字参数 只接收job，city作为关键字参数的参数组合
    print('name:',name,'age',age,'job',job,'city',city)

# 参数组合定义的顺序必须是:必选参数  默认参数  可变参数  命名关键字参数  关键字参数
if __name__ == "__main__":
    person2('swj',12,job='java',city='hangzhou')
