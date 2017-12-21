# -*- coding: utf-8 -*-

import pickle
# d = dict(name='bob', age=20, score=88)
# print(pickle.dumps(d))
#
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)  # 直接把对象序列化之后写入一个file-like Object
# f.close()
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
# 两个变量完全是不同的对象 只是内容相同
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
