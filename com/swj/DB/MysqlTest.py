# -*- coding: utf-8 -*-

import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(user='root', password='swj19961226', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)
finally:
    cursor.close()
    conn.close()


