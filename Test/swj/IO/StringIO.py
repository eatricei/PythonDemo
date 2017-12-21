# -*- coding: utf-8 -*-

# 在内存中读写String
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('大傻逼')
# print(f.getvalue())  # getvalue()用于获得写入后的String

# f = StringIO('hello,\nworld\n')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# 在内存中读写二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
