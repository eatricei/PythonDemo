# -*- coding: utf-8 -*-
# hmac keyed-hashing for message authentication
# 通过一个标准算法在计算hash的过程中 把key混入计算过程中 针对所有哈希算法都通用
# 采用hmac替代我们自己写的salt算法 可以使程序更加标准化更加安全

import hmac
import random
message = b'Hello, World!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长可以多次调用h.update(msg)
print(h.hexdigest())  # 输出长度和原始哈希算求相同
# 需要注意传入的key和message都是bytes类型 str类型需要编码为bytes

# login using hmac


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


if __name__ == '__main__':
    print(login('michael', '123456'))
