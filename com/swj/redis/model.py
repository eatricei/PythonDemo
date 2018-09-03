# -*- coding: utf-8 -*-
import redis
from com.swj import const
# redis连接
# r = redis.Redis(host=const.Linux().IP, port=6379, db=0)
# r.set('name', '张三')
# print(r.get('name').decode('utf-8'))  # 字节流的解码
# r.close()

# redis连接池 避免每次建立、释放连接的开销
pool = redis.ConnectionPool(host=const.Linux().IP, port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', '儿子')
print(r.get('name').decode('utf-8'))

# 参数
# set(name, value, ex=None, px=None, nx=False, xx=False) ex:过期时间（秒）px:过期时间（毫秒）nx:为True，name不存在才执行
# xx:为True时，name存在才执行
# setex(name, value, time) 设置过期时间（秒）
# psetex(name, time_ms, value) 设置过期时间（豪秒）
# 批量设置值


# 管道 默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，
# 则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。
pipe = r.pipeline(transaction=True)
r.set('name', '妈妈')
r.set('name', '爸爸')
pipe.execute()
print(r.get('name').decode('utf-8'))

