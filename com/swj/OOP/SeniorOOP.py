# -*- coding: utf-8 -*-
# __slots__
# 正常情况下 当我们定义一个class 创建了一个class实例后 我们可以给该实例绑定任何属性和方法 ——动态语言的灵活性
# 但是我们要限制实例的属性 就要定义一个特殊的变量__slots__
# class Student(object):
#     __slots__ = ('name', 'age')  # tuple定义允许绑定的属性名称
#
# s = Student()
# s.name = 'swj'
# s.age = 20
#
# # 需要注意的是__slots__定义的属性仅对当前类实例起作用 对继承的子类不起作用 除非在子类中也定义__slots__ 子类允许的属性就是子类+父类
# class GraduateStudent(Student):
#     __slots__ = ('sb')

# @property
# 在绑定属性时 如果直接把属性暴露出去 虽然写起来简单 但是没办法检查参数 导致可以随意更改
# 一种方式是前面封装提到过的用get set方法的方式 但是略复杂
# 与decorator给函数动态加上功能 对类方法我们可以采用@property装饰器就是负责把一个方法变成属性调用的
#
# class Student(object):
#     @property   # 将一个getter方法变成属性 本身又创建了一个装饰器@score.setter
#     def score(self):
#         return self._score
#
#     @score.setter   # 负责将一个setter方法变成属性赋值
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0·100!')
#         self._score = value
#
# s = Student()
# s.score = 60  # 实际转化为s.set_score(60)
# print(s.score)  # 实际转化为s.get_score()
# s.score = 999

# 多重继承
# mixin设计 ——给一个类增加多个功能
# python 中的 MRO

# 特殊用途的函数帮助我们定制类

# __str__


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student Object (name:%s)'% self.name
#     __repr__ = __str__
# s = Student('Swj')
# print(s)  # 调用__str__ 返回用户看到的字符串
# s  # 调用__repr__ 返回程序开发者看到的字符串 解决方法是再定义一个__repr__通常与__str__相同

#  __iter__ 使类可以被迭代 返回一个迭代对象 调用__next__方法不断拿到循环的下一值
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a +self.b
#         if self.a >100000:
#             raise StopIteration
#         return self.a
# for n in Fib():
#     print(n)

# __getitem__ Fib实例虽然能被作用于for循环 但是不能拿到指定元素

# class Fib(object):
#     def __getitem__(self, item):
#         a, b = 1, 1
#         for x in range(item):
#             a, b = b, a+b
#         return a
# f = Fib()
# print(f[5])  # 使Fib实例看上去像个list 但不能使用切片
#
# class Fib(object):
#     def __getitem__(self, item):
#         a, b = 1, 1
#         if isinstance(item, int):
#             for x in range(item):
#                 a, b = b, a+b
#             return a
#         if isinstance(item, slice):
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a+b
#             return L
# f = Fib()
# print(f[2:6])  # 实现切片 但是没对step参数进行处理 也没对负数进行处理
#
# # 还有__setitem__() __delitem__()方法 总之 可以使我们自定义的类表现的和list tuple dict 没什么区别 归功于‘鸭子类型’
#
# # __getattr__ 正常情况下 当我们调用类的方法或属性时 如果不存在就会报错 Attribute Error
# # 当调用不存在的属性时(只有在没有找到这个属性时) 解释器就会试图调用__getattr__(self, 'score')来尝试获得属性
# class Student(object):
#     def __init__(self):
#         self.name = 'swj'
#     def __getattr__(self, item):  # 默认返回None
#         if item == 'score':
#             return 99
#         if item == 'age':  # 返回函数完全可以
#             return lambda: 20
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)  # 保持约定
# s = Student()
# print(s.score)
# print(s.age())


# class Chain(object):
#
#     def __init__(self, path=''):
#         self.__path = path
#
#     def __getattr__(self, path):
#         # if path == 'users':
#         #     return lambda user: Chain('%s/%s/%s' % (self.__path, path, user))
#         return Chain('%s/%s' % (self.__path, path))
#
#     def __call__(self, user):
#         return Chain('%s/%s' % (self.__path, user))
#
#     def __str__(self):
#         return self.__path
#     __repr__ = __str__
#
# print(Chain().users('swj').repos)
#
# # __call__ 一个对象实例可以有自己的方法和属性 instance.method() 还可以直接在实例上调用
#
#
# class Student(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print('My name is %s ' % self.name)
#
# s = Student('swj')
# s()

# 通过callable()函数 我们可以判断一个对象是否是'可调用'对象

# 使用枚举类  把一组相关常量定义在一个class中，且class不变 成员可以相互比较

# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)  # value 自动赋值为int 默认从0开始

# from enum import Enum, unique
#
#
# @unique  # 保证没有重复值
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# print(Weekday.Tue.value)
# print(Weekday(2))

# 使用元类
# 静态语言和动态语言最大的不同在于函数和类的定义 不是编译时定义的 而是运行时动态定义的
# type()
# print(type(Student))  # <class 'type'>
# class的定义是运行时动态创建的 而创建class的方法就是使用type()函数
# type()既可以返回一个对象的类型 又可以创建出新的对象

# def fn(self, name='world'):  # 先定义函数
#     print('Hello, %s.' % name)
# Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class 三个参数 class名称 继承的父类集合(注意tuple的单元素写法) class的方法名称与函数名称绑定
# h = Hello()
# h.hello('swj')

# metaclass 控制类的创建行为
# 先定义metaclass 再创建类 最后创建实例
# metaclass允许你创建和修改类
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):  # 当前准备创建的类的对象 类的名字 类继承的父类集合 类的方法集合
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)

# ORM(Object Relational Mapping) 对象-关系映射 把关系数据库的一行映射为一个对象 也就是一个类对应一个表 不用直接操作SQL
# 要编写ORM框架所有的类只能动态定义 因为只有使用者才根据表的结构来定义出对应的类

