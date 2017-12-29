# -*- coding: utf-8 -*-
# 把一个32位无符号整数变成字节，也就是4个长度的bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# 利用Struct模块
import struct
print(struct.pack('>I',n))  # pack的第一个参数是处理指令 >表示字节顺序是big-endian 也就是网络序 I表示4字节无符号整数
