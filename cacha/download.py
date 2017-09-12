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
class Download(object):
    #下载类
    def __int__(self,user_agent=None,proxies=None,num_retires=None,\
                cache=None):
        self.user_agent=user_agent
        self.proxies=proxies
        self.num_retries=num_retires #重试次数
        self.cache=cache
    def __call__(self, url,):
        result=None
        if self.cache:
            try:
                result=self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries>0 and 500<=result['code']
                    return None




if __name__=='__main__':
    d=Download()
    d()

