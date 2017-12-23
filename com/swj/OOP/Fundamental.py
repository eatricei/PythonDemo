# -*- coding: utf-8 -*-
# class Student(object):  # 表示从object类中继承
#     pass
# bart = Student()
# print(bart)
# print(Student)
# bart.name = 'swj'
# print(bart.name)

# class Student(object):
#     def __init__(self, name, score):  # 第一个参数永远是self表示创建的实例本身 不用传 其他参数需要传
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s:%s'%(self.name, self.score))
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# bart = Student('swj', 99)
# print(bart.get_grade())
#
# # 数据封装
# bart.print_score()

# 访问权限 实例变量以__开头就变成了私有变量

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s:%s'%(self.__name, self.__score))
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
# s = Student('swj', 99)
# # print(s.__name)  # 无法访问
# print(s.get_name())
# s.print_score()
#
# # 类似__xx__的实例变量名 是特殊变量(以双下划线开头以双下划线结尾) 可以直接访问 但是不能用__name__ __score__这样的变量名
# # 以单下划线开头的变量 外部可以访问 但是“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
# print(s._Student__name)  # 私有变量也可以访问 但是强烈建议不要这么做 私有变量被内部包装为_Student__name
# s._Student__name = 'xhy'
# print(s.get_name())

# 继承与多态
class Animal(object):
    def run(self):
        print('animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running...')
    def eat(self):
        print('dog is eating...')

class Cat(Animal):
    def run(self):
        print('cat is running...')
    def eat(self):
        print('cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()
Dog().run()
Cat().run()
run_twice(Animal())
run_twice(Dog())  # 多态
# 开闭原则  对扩展开放：允许新增Animal子类 对修改封闭:不需要修改run_twice()等接受Animal类型的函数
# 静态语言VS动态语言  静态语言必须要传入Animal或子类 否则就无法调用run()方法 动态语言则只需保证传入的对象一个run()方法 ----鸭子类型（file-like object）

# 获取对象信息
type(123)  # int
type('str')  # str
type(None)  # NoneType
type(abs)  # builtin_function_or_method
type(Animal())  # __main__.Animal
# 更多的type在types模块中定义
# 对于class的继承关系 使用type()不方便 可以用isinstance() 函数 优先使用isinstance()

# 使用dir()函数获得一个对象的所有属性和方法 返回包含str的list
dir('dir')
# len('ABC') 和'ABC'.__len__() 也可以自定义len方法

class MyDog(Dog):
    def __len__(self):
        return 100

print(len(MyDog()))

# 通过getattr()、setattr()、hasattr()可以直接操作一个对象的状态
# 类属性与实例属性 不要对实例属性和类属性使用相同的名字  会屏蔽掉类属性
