#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/13 下午 20:11
@Author  : chaoyifei
@File    : diskcache.py
@Software: PyCharm
'''
import os
from link_crawler import link_crawler
import pickle
import datetime
from datetime import timedelta
import urlparse
import re



class DiskCache(object):
    def __init__(self,cache_dir='cache',expires=timedelta(days=1)):
        self.cache_dir=cache_dir
        self.expires=expires
    def url_to_path(self,url):
        componets=urlparse.urlsplit(url)
        path=componets.path
        if not path:
            path='/index.html'
        elif path.endswith('/'):
            path+='index.html'
        filename=componets.netloc+path+componets.query
        filename=re.sub('[^/0-9a-zA-Z\-.,;_]',filename)
        filename='/'.join(segment[:255]for segment in filename.splite('/'))
        return os.path.join(self.cache_dir,filename)
    def __getitem__(self, url):
        path=self.url_to_path(url)
        if os.path.exists(path):
            with open(path,'rb') as fp:
                result,timestamp=pickle.loads(fp.read())
                if self.has_expired(timestamp):
                    raise KeyError(url,'has expired')
                return result
    def has_expired(self,timestamp):#获取当前时间和缓存的时间加上过期时间对比
         return datetime.datetime.utcnow()>timestamp+self.expires
    def __setitem__(self, url,result):
        timestamp=datetime.datetime.utcnow()
        data=pickle.dumps(result,timestamp)
        path=self.url_to_path(url)
        folder=os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path,'wb') as fb:
            fb.write(data)
if __name__=='__main__':
    link_crawler('http://example.webscraping.com/','/(index|view)',max_depth=1,cache=DiskCache())