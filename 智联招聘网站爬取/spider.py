#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/03/24 下午 19:56
@Author  : chaoyifei
@File    : spider.py
@Software: PyCharm
'''
from datetime import datetime
import urllib
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import pymongo
from config import *
import time
from itertools import product
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]

def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    response = requests.get(url, headers=headers)
    return response.text

def get_content(html):
    # 记录保存日期
    date = datetime.now().date()
    date = datetime.strftime(date, '%Y-%m-%d')  # 转变成str

    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find('div', {'class': 'newlist_list_content'})

    if data_main:
        tables = data_main.find_all('table')

        for i, table_info in enumerate(tables):
            if i == 0:
                continue
            tds = table_info.find('tr').find_all('td')
            zwmc = tds[0].find('a').get_text()  # 职位名称
            zw_link = tds[0].find('a').get('href')  # 职位链接
            fkl = tds[1].find('span').get_text()  # 反馈率
            gsmc = tds[2].find('a').get_text()  # 公司名称
            zwyx = tds[3].get_text()  # 职位月薪
            gzdd = tds[4].get_text()  # 工作地点
            gbsj = tds[5].find('span').get_text()  # 发布日期

            tr_brief = table_info.find('tr', {'class': 'newlist_tr_detail'})
            # 招聘简介
            brief = tr_brief.find('li', {'class': 'newlist_deatil_last'}).get_text()

            # 用生成器获取信息
            yield {'zwmc': zwmc,  # 职位名称
                   'fkl': fkl,  # 反馈率
                   'gsmc': gsmc,  # 公司名称
                   'zwyx': zwyx,  # 职位月薪
                   'gzdd': gzdd,  # 工作地点
                   'gbsj': gbsj,  # 公布时间
                   'brief': brief,  # 招聘简介
                   'zw_link': zw_link,  # 网页链接
                   'save_date': date  # 记录信息保存的日期
                   }

def main(args):
    basic_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'

    for keyword in KEYWORDS:
        mongo_table = db[keyword]
        paras = {'jl': args[0],
                 'kw': keyword,
                 'p': args[1]  # 第X页
                 }
        url = basic_url + urllib.urlencode(paras)
        # print(url)
        html = download(url)
        # print(html)
        if html:
            data = get_content(html)
            for item in data:
                if mongo_table.update({'zw_link': item['zw_link']}, {'$set': item}, True):
                    item=json.dumps(item,ensure_ascii=False)
                    print'已保存记录：',item

if __name__ == '__main__':
    start = time.time()
    number_list = list(range(TOTAL_PAGE_NUMBER))
    args = product(ADDRESS, number_list)
    pool = Pool()
    pool.map(main, args)# 多进程运行
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))