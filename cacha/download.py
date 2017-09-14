#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/12 下午 19:17
@Author  : chaoyifei
@File    : download.py
@Software: PyCharm
'''
import urlparse
import urllib2
import random
#下载类
class Download(object):

    def __init__(self,user_agent=None,proxies=None,num_retries=None, cache=None):
        self.user_agent=user_agent
        self.proxies=proxies
        self.num_retries=num_retries #重试次数
        self.cache=cache
    def __call__(self, url,):
        result=None
        if self.cache:
            try:
                result=self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries>0 and 500<=result['code']:
                    return None
        if result is None:
            proxy=random.choice(self.proxies) if self.proxies else None
            headers={'User-agent':self.user_agent}
            result=self.download(url,headers,proxy,self.num_retries)
            if self.cache:
                self.cache[url]=result #把数据存入缓存
    def download(self,url,headers,proxy,num_retries,data=None):
        print 'Download:',url
        request=urllib2.Request(url,headers=headers)
        try:
            response=urllib2.urlopen(request)
            html=response.read()
            code=response.code
        except urllib2.URLError as e:
            print 'Download error',e.reason #打印错误信息
            html=None
            if hasattr(e,'code'):  #查找
                code=e.code
                if num_retries>0 and 500<=code<600:
                    return self.download(url,headers=headers,\
                                         proxy=proxy,num_retries=num_retries-1)
                else:
                    code=None
        return {'html':html,'code':code}






if __name__=='__main__':
    d=Download()


