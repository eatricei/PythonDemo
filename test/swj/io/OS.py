# -*- coding: utf-8 -*-
import os
print(os.name)  # 操作系统类型
# print(os.uname())  # 详细信息 windows不支持
print(os.environ)  # 环境变量
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

print(os.path.abspath('.'))  # 查看当前目录的绝对路径
print(os.path.join('test'))  # 合成路径
os.path.split('')  # 拆分路径
os.path.splitext('')  # 可以获得文件的扩展名

# print(os.mkdir('test'))
print(os.rmdir('test'))

os.rename('原名', '新名')
os.remove('')

# shutil --os模块的补充
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
