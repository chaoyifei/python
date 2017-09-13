#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/12 下午 19:55
@Author  : chaoyifei
@File    : link_crawler.py
@Software: PyCharm
'''
import  re
import urlparse
import robotparser
from download import Download

def link_crawler(seed_url,link_regex=None,max_depth=1,user_agent='wawp',proxies=None,num_retries=1,cache=None):
    crawl_queue= [seed_url] #url存放列表
    seen= {seed_url:0} #判断爬取深度
    num_urls=0 #总共下载多少页
    rp=get_robots(seed_url)
    D=Download(user_agent=user_agent,proxies=proxies,num_retries=num_retries,cache=cache)


    while crawl_queue:
        url=crawl_queue.pop() #取出list里边最后一个url
        depth=seen[url] #把当前url的请求次数赋值
        if rp.can_fetch(user_agent,url):
            html=D(url)
            links=[]
            if depth !=max_depth:
                if link_regex:
                    links.extend(link for link in get_links(html,link_regex) if re.search(link_regex,links) ) #添加list
            for link in links:
                 link=normalize(seed_url,link) #拼接url
                 if link not in seen:
                     seen[link]=depth+1
                     if same_domain(seed_url,link):
                         crawl_queue.append(link)


def get_robots(url):
    rp=robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url,'/robots.txt'))
    rp.read()
    return rp
def get_links(html):
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE) #忽略大小写
    return webpage_regex.findall(html)
def normalize(seed_url,link):
    return urlparse.urljoin(seed_url,link)
#检查域名
def same_domain(seed_url,link):
    return urlparse.urlparse(seed_url).netloc==urlparse.urlparse(link).netloc
