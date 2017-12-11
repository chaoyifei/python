# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib import urlencode
import pymongo
import json
from requests.exceptions import ConnectionError
from hashlib import md5
import os
from simplejson import JSONDecodeError
import re
from multiprocessing import Pool


Mongo_url="192.168.3.113"
Mongo_db="jiepai"
Mongo_table="jiepai"
#连接mongodb数据库
client=pymongo.MongoClient(host=Mongo_url, port=27017)
db=client[Mongo_db]
def get_page_index(offset):
    data={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'cur_tab':3
    }
    params=urlencode(data) #将字典构造为URL
    base='https://www.toutiao.com/search_content/?'
    url=base+params
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0'}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        print ('Error occurred')
        return None
def download_image(url):
    print ('Downloading',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            save_image=(response.content)
        return None
    except ConnectionError:
        return None
def save_image(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print (file_path)
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close
def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None
def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    result=soup.select('title')
    title=result[0].get_text() if result else ''
    images_pattern=re.compile(r'gallery: (.*?),\n')
    result=re.search(images_pattern, html)
    if result:
        data=json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            #返回标题，此详情页的URL，和图片的url列表
            return {
                    'title':title,
                    'url':url,
                    'images':images
                    }
        else:
            pass
def save_to_mongo(result):
    if db[Mongo_table].insert(result):
        print ('Successfully Saved to Mongo',result)
        return True
    return False
def main(offset):
    text = get_page_index(offset)
    urls = parse_page_index(text)
    for url in urls:
        html = get_page_detail(url)
        result = parse_page_detail(html, url)
        if result: save_to_mongo(result)
pool = Pool()
groups = ([x * 20 for x in range(1, 21)])
pool.map(main, groups)
pool.close()
pool.join()
