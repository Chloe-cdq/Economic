#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sqlite3

#此函数将爬取到的数据要存⼊本地数据库
def create_database(data):
    # 连接数据库
    conn = sqlite3.connect('Price.db')
    #创建定位指针
    c = conn.cursor()
    #创建表
    try:
        c.execute("DROP TABLE price")
    except:
        pass
    c.execute('''CREATE TABLE price(id INT PRIMARY KEY, item TEXT, year TEXT, quantity REAL);''')

    #将从网络得到的数据存入数据库
    for i in data["returndata"]["datanodes"]:
        if i["data"]["hasdata"] == True \
                and (i["wds"][0]["valuecode"]=='A090101'\
                or i["wds"][0]["valuecode"]=='A090102' \
                or i["wds"][0]["valuecode"]=='A090103'):
            c.execute("INSERT INTO price (item,year,quantity) VALUES (?, ?, ?);",
                      (i["wds"][0]["valuecode"], i["wds"][1]["valuecode"], i["data"]["data"]))

    #提交操作并关闭数据库
    conn.commit()
    conn.close()