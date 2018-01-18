# -*- coding: utf-8 -*-

# asyncio 是python3.4版本引入的标准库 内置了对异步IO的支持
#  asyncio的编程模型就是一个消息循环
import asyncio

@asyncio.coroutine
def hello():
    print("hello,world!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello, again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
