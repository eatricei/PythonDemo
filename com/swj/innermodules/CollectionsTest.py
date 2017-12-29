# -*- coding: utf-8 -*-
# namedtuple
# 是一个函数 用来创建一个自定义的tuple对象
# tuple表示不变集合 比如表示一个二维坐标 p=(1,2) 但是很难看出是坐标
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, tuple))

# list存储数据时 按索引访问元素很快，但是插入和删除元素很慢
# deque 高效实现插入删除操作的双向列表 适用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# dict 如果引用的key不存在 就会抛出一个KeyError,如果想要key不存在时返回一个default值就用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')  # 调用函数返回
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# dict key是无序的 在对dict做迭代的时候我们无法确定key的顺序 , 可以用OrderedDict 来保持key的顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # 按照插入的顺序排列 不是key本身排序
# 可以实现一个FIFO（先进先出） 的dict 当容量超过限制，先删除最早添加的Key

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key,value))
        else:
            print('add:', (key,value))
        OrderedDict.__setitem__(self, key, value)

# Counter 简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
