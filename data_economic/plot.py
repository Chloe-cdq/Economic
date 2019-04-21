#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sqlite3

#此函数从本地数据库读取数据并绘制折线图与条形图
def create_plot():
    # 设置中文字体和负号正常显示
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    year10 = list(range(2009, 2019, 1))#用来存储十年年份
    year20 = list(range(1999, 2019, 1))#用来存储二十年年份
    gdp = []#用来存储二十年gdp
    incre1 = []#用来存储十年第一类产业增加值
    incre2 = []#用来存储十年第二类产业增加值
    incre3 = []#用来存储十年第三类产业增加值

    #连接数据库并读取数据
    conn = sqlite3.connect('Economic.db')
    c = conn.cursor()
    c.execute("select year,item,quantity from economic;")
    data_fetch = c.fetchall()
    conn.close()

    #整合数据，存入相应变量（gdp,incre1,incre2,incre3)
    data = {'1999':{},'2000':{},'2001':{},'2002':{},'2003':{},'2004':{},'2005':{},'2006':{},
            '2007': {},'2008':{},'2009':{},'2010':{},'2011':{},'2012':{},'2013':{},'2014':{},
            '2015':{},'2016':{},'2017':{},'2018':{},}#嵌套字典，用于整合数据
    for i in data_fetch:
        data[i[0]][i[1]] = i[2]
    for i in year20:
        gdp.append(data[str(i)]['A020102'])
    for i in year10:
        incre1.append(data[str(i)]['A020103'])
        incre2.append(data[str(i)]['A020104'])
        incre3.append(data[str(i)]['A020105'])

    # 绘制二十年gdp折线图
    plt.figure(figsize=(16, 4))#设置画布大小
    plt.plot(year20, gdp)#利用相关数据绘制折线图
    # 设置图表标题，并给坐标轴加标签
    plt.title("1999-2018年国内生产总值", fontsize=14)
    plt.xlabel("年份", fontsize=10)
    plt.ylabel("国内生产总值（亿元）", fontsize=10)
    # 设置折线上数据点的数字标签
    for x, y in zip(year20, gdp):
        plt.text(x, y, '%.01f'%y, ha='center', va='bottom', fontsize=10)
    # 设置x轴刻度标记的大小
    plt.xticks(np.arange(min(year20) - 1, max(year20) + 1, 1.0))
    #设置坐标轴的参数
    plt.tick_params(axis='both', labelsize=10)
    #展示
    plt.show()

    #绘制十年三类产业增加值条形图
    plt.figure(figsize=(16, 4))#设置画布大小
    bar_width = 0.3#条形宽度
    #利用相关数据绘制条形图
    rects1 = plt.bar(x=year10, height=incre1, width=bar_width, color='red', label="第一类产业")
    rects2 = plt.bar(x=[i + bar_width for i in year10], height=incre2, width=bar_width, color='green', label="第二类产业")
    rects3 = plt.bar(x=[i + 2*bar_width for i in year10], height=incre3, width=bar_width, color='blue', label="第三类产业")
    # 设置图表标题，并给坐标轴加标签
    plt.title("三类产业在2009-2018年内的增加值")
    plt.xlabel("年份")
    plt.ylabel("增加值（亿元）")
    # 设置x轴刻度标记的大小
    plt.xticks(np.arange(min(year10) - 1, max(year10) + 1, 1.0))
    # 设置坐标轴的参数
    plt.tick_params(axis='both', labelsize=10)
    # 设置图例
    plt.legend()
    # 设置条形图上数据点的数字标签
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, '%.01f'%height, ha="center", va="bottom")
    for rect in rects2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, '%.01f'%height, ha="center", va="bottom")
    for rect in rects3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, '%.01f'%height, ha="center", va="bottom")
    #展示
    plt.show()