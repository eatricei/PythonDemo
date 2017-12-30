# -*- coding: utf-8 -*-
import itertools


def main():
    natuals = itertools.count(1)  # count()会创建一个无限迭代器
    # for n in natuals:
    #     print(n)
    # cs = itertools.cycle('ABC')  # 字符串也是序列的一种 cycle()无限重复
    # for c in cs:
    #     print(c)
    # ns = itertools.repeat('ABC', 3)  # 将一个元素无限重复下去 如果提供第二个参数就是重复的次数
    # for n in ns:
    #     print(n)
    # 无限序列只有在for迭代时才会无限迭代下去
    # 并且可以通过takewhile()等函数来截取
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns))
    for c in itertools.chain('ABC', 'XYZ'):  # 迭代对象串联起来
        print(c)
    for key, group in itertools.groupby('AAABBCCAA'):  # 将迭代器中相邻的重复元素挑出来放在一起  其实是通过函数完成的
        print(key, list(group))
    for key, group in itertools.groupby('AaAbBCcAA', lambda x: x.upper()):
        print(key, list(group))


def pi(N):
    # odd = itertools.count(1, 2)
    # ss = itertools.takewhile(lambda x: x <= N*2, odd)
    # sum = 0
    # flag = True
    # for i in ss:
    #     if flag:
    #         sum += 4/i
    #     else:
    #         sum += -4/i
    #     flag = not flag
    # return sum
    return sum(map(lambda x: (-1)**(x//2)*4/x, itertools.takewhile(lambda x: x <= N*2, itertools.count(1, 2))))
if __name__ == '__main__':
    print(pi(10))
