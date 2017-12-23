# -*- coding: utf-8 -*-
import functools
# import time
# def metric(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         start = time.time()
#         fun = func(*args, **kw)
#         print('%s:%s'%(func.__name__,time.time()-start))
#         return fun
#     return wrapper
# @metric
# def hello():
#     pass
#
# hello()
import types
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text,types.FunctionType):
                print('%s'%func.__name__)
            else:
                print('%s'%text)
            return func(*args, **kw)
        return wrapper
    if isinstance(text,str):
        return decorator
    else:
        return decorator(text)
@log('dsd')
def hello():
    print('swj')

hello()