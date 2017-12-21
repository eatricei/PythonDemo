# -*- coding: utf-8 -*-
import json
# d = dict(name='Bob',age=20,score=88)
# j = json.dumps(d)  # str类型  序列化 dump 方法直接把JSON写入一个file-like Object
# print(type(j))
# s = json.loads(j)  # dict类型 反序列化
# print(type(s))
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
# # 转换函数
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
# print(json.dumps(s, default=lambda obj: obj.__dict__))  # 把任意一个Object的实例转为dict(除了定义__slots__的class)

# 同样把一个JSON数据转为Python的对象实例也需要转换出一个dict对象
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
# json_str = '{"age":20,"score":88,"name":"Bob"}'
# print(json.loads(json_str,object_hook=dict2student))

# 中文进行序列化时 json.dumps()提供了一个ensure_ascii参数
obj = dict(name='小明', age=20)
print(json.dumps(obj, ensure_ascii=False))  # 指定ensure_ascii参数为False
