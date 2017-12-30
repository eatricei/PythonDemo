# -*- coding: utf-8 -*-
# 摘要算法 如MD5，SHA1等等 又称哈希算法、散列算法  不算加密算法不能用于加密
# 通过一个函数把任意长的数据转换为一个长度固定的数据串(通常用16进制的字符串表示)
# 单向函数 计算很容易 但是反推很困难

# md5 MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# SHA1 SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if md5.hexdigest() == db.get(user):
        return True
    else:
        return False

if __name__ == '__main__':
    print(login('michael', '123456'))