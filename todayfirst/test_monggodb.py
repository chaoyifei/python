# -*- coding:utf-8 -*-
from pymongo import MongoClient
conn=MongoClient(host='192.168.3.113', port=27017, document_class=dict, tz_aware=None, connect=None)
db=conn.mydb #连接数据库db，没有则自动创建
my_set=db.test_set#使用test_set集合，没有则自动创建
my_set.insert({"name":"zhangsan","age":18})#插入数据

for i in my_set.find():#取出数据
    print(i)
