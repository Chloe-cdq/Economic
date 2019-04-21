#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import time
import json
# 用来获取时间戳
def gettime():
    return int(round(time.time() * 1000))

#此函数爬取国家统计局的数据库data.stats.gov.cn中的数据
def get_data_from_network():
    headers = {}# 用来自定义头部的
    keyvalue = {}# 用来传递参数的
    url = 'http://data.stats.gov.cn/easyquery.htm'# 目标网址
    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)' \
                            'AppleWebKit/537.36 (KHTML, like Gecko)' \
                            'Chrome/70.0.3538.110 Mobile Safari/537.36'
    # 参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0201"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    session = requests.session()
    # 在Session基础上进行一次请求
    session.post(url, params=keyvalue, headers=headers)
    # 修改dfwds字段内容以获取二十年内的数据
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    data = session.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码及数据
    print(data.status_code)
    data=json.loads(data.text)
    print(data)

    #返回获得的数据
    return data