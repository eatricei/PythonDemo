# -*- coding: utf-8 -*-
# try:
#     f=open('E:/c/nmsl/5.10.c','r')
#     print(f.read())
# finally:
#     f.close()

# with open('E:/c/nmsl/5.10.c','r') as f:
#     print(f.read())
# with open('E:/c/nmsl/5.10.c','r') as f:
#     for line in f.readlines():
#         print(line.strip())

# file-like Object ----像open()函数返回的这种有个read()方法的对象

# StringIO就是在内存中创建的file-like Object 常用作临时缓冲

# f = open('C:/Users/swj/Pictures/Feedback/{A9FD0FA9-9FF1-474F-9B57-0115324C87F8}/Capture001.png', 'rb')
# print(f.read())  # 十六进制表示的字节

# f = open('E:/c/1.txt', 'r', encoding='UTF-8', errors='ignore')
# print(f.read())

# f = open('E:/c/1.txt', 'w', encoding='utf-8')
# f.write('hello,大傻逼')
# f.close()

with open('E:/c/1.txt', 'w', encoding='utf-8') as f:
    print(f.write('大傻逼'))
