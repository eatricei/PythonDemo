# -*- coding: utf-8 -*-
# 二进制到字符串的转换方法 Base64 就是一种最常见的二进制编码方法
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')