# -*- coding: utf-8 -*-
import redis
import time
from com.swj import const

# 平均1800次/s
r = redis.Redis(host=const.Linux().IP, port=6379, db=0)
start = time.time()
i = 0
while True:
    end = time.time()
    if end > start + 1:
        break
    i = i + 1
    r.set('test' + str(i), str(i) + '')

print('redis每秒操作：' + str(i) + '次')