# -*- coding: utf-8 -*-
# 任何对象 只要正确实现了上下文管理 就可以使用with语句
# 实现上下文管理通过 __enter__ 和 __exit__这两个方法实现


# class Query(object):
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print('Begin')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# if __name__ == '__main__':
#     with Query('Bob') as q:
#         q.query()

# 通过__enter__和__exit__还是太繁琐 contextlib提供更简单的写法
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)
if __name__ == '__main__':
    # with create_query('Bob') as q:
    #     q.query()
    with tag('swj'):  # with 语句首先执行yield之前的语句 所以先打印出<swj>
        print('hello')  # yield 调用会执行with语句内部的所有语句
        print('world')  # 最后执行yield后面的语句
