#coding:utf-8
#爬取豆瓣电影top250存到excel中
'''
Created on 2017年7月12日

@author: Administrator
'''
import requests,re
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Color
import sys
reload(sys)

default_encoding = 'utf-8'
wb=Workbook()
dest_filename= u'电影.xlsx'
ws1=wb.active
ws1.title=u"豆瓣电影top250"

download_url='http://movie.douban.com/top250/'

def download_page(url):
    '''获取url页面内容 '''
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    data=requests.get(url,headers=headers).content
    return data

def get_li(doc):
    soup=BeautifulSoup(doc,'html.parser')
    
    ol=soup.find('ol',class_='grid_view')
    
    name=[]#名字
    star_con=[]#评论人数
    score=[]#评分
    info_list=[]#短评
    
    for i in ol.find_all('li'):
        detail=i.find('div',attrs={'class':'hd'})
        movie_name=detail.find('span',attrs={'class':'title'}).get_text() #电影名
        level_star=i.find('span',attrs={'class':'rating_num'}).get_text()#评分
        star=i.find('div',attrs={'class':'star'})
        star_num = star.find(text=re.compile(u'评价'))  #评价 u转码
 
        
        info=i.find('span',attrs={'class':'inq'})
        if info:
            info_list.append(info.get_text())
        else:
            info_list.append('无')
        score.append(level_star)
        
        name.append(movie_name)
        star_con.append(star_num)
    page=soup.find('span',attrs={'class':'next'}).find('a')
    
    if page:
        return name,star_con,score,info_list,download_url+page['href']
        
    return name,star_con,score,info_list,None


def main():
    url = download_url
    name = []
    star_con=[]
    score = []
    info = []
    while url:
        doc = download_page(url)
        movie,star,level_num,info_list,url = get_li(doc)
        name = name + movie
        star_con = star_con + star
        score = score+level_num
        info = info+ info_list
    for (i,m,o,p) in zip(name,star_con,score,info):
        ws1['A1'] = u'电影名'
        ws1['B1'] = u'评论数'
        ws1['C1'] = u'评分'
        ws1['D1'] = u'短评'
        ws1.cell('A1').styles.font.color.index=Color.red
        col_A = 'A%s'%(name.index(i)+2)
        col_B = 'B%s'%(name.index(i)+2)
        col_C = 'C%s'%(name.index(i)+2)
        col_D = 'D%s'%(name.index(i)+2)
        ws1[col_A]=i
        ws1[col_B] = m
        ws1[col_C] = o
        ws1[col_D] = p
    wb.save(filename=dest_filename)
    
 
if __name__ == '__main__':
    main()    
    
    
    
    
    

