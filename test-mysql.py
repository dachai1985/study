# _*_ coding: utf-8 _*_

import os, sqlite3
from sqlite3.dbapi2 import Cursor

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#初始数据：
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #'返回指定分数区间的名字，按分数从低到高排序'
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    #cursor.execute('select name, score from user')
    cursor.execute('select name, score from user order by score')

    socre_sort = cursor.fetchall()
    cursor.close()
    conn.close()

    #socre_sort = sorted(values, key=lambda e: e[1], reverse=False)
    #print(socre_sort)

    names = []
    for x in socre_sort:

        if x[1] >= low and x[1] <= high:
            #names += x[0] + ', '
            names.append(x[0])

    #names = names[0: -2]
    print('name============', names)
    return names

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')




'''
import mysql.connector

conn = mysql.connector.connect(host="10.34.4.251",user="test",passwd="123456",db="mytable")
cursor = conn.cursor()

cursor.execute('select * from alpha_common.hbaccess where dt=? and cid=? order by ts desc limit 10', ('20200904', 'LGSCAFE'))

myresult = cursor.fetchall()
for x in myresult:
    print(x)

cursor.close()
conn.close()
'''