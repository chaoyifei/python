#coding:utf-8
import scrapy
from bs4 import BeautifulSoup
import os 
import urllib
import urllib2
import zlib
import requests
class photo(scrapy.Spider):
    name="photo"
    def start_requests(self):
        
        #www.xedq8.com
        
        
        urls = ['http://www.xedq8.com/shenshi']
        for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        #返回html源码
        content=response.body
        if not content:
            self.log('parse body error')
            return
        #用BeautifulSoup进行解析
        soup=BeautifulSoup(content,'html5lib')
        # 获取包含漫画列表的标签
        
        listcon_tag=soup.find('ul',class_='listcon')
        if len(listcon_tag)<1:
            self.log('extract photo list error')
            return
        
        # 列表中每部漫画的<a>标签
        com_a_list=listcon_tag.find_all('a',attrs={'href':True})
        if len(com_a_list)<1:
            self.log('Can not find <a> that contain href attribute.')
            return
        #获取列表中的URL
        comics_url_list=[]
        
        base='http://www.xedq8.com'
        for tag_a in com_a_list:
            url=base+tag_a['href']
            comics_url_list.append(url)
        print('\n>>>>>>>>>>>>>>>>>>> current page photo list <<<<<<<<<<<<<<<<<<<<')
        print(comics_url_list)
        
        #处理当前页面的每部漫画
        for url in comics_url_list:
            print('>>>>>>>>  parse comics:' + url)
            yield scrapy.Request(url=url,callback=self.comics_parse)
        
        #漫画列表下方的选页栏
        page_tag=soup.find('u1',calss_='pagelist')
        if len(page_tag)<1:
            self.log('extract page tag a error.')
            return
        
        # 根据select控件来判断当前是否为最后一页
        select_tag=soup.find('select',attrs={'name','sldd'})
        option_list=select_tag.find_all('option')
        # 最后一个option标签，若有 selected 属性，则说明为最后一页
        last_option = option_list[-1]
        current_option = select_tag.find('option' ,attrs={'selected': True})

        is_last=(lsat_option.string==current_option.string)
        if not is_last:
            #最后一个为末页，倒数第二个为下一页
            next_page = 'http://www.xedq8.com/shenshi/' + page_a_list[-2]['href']
            if next_page is not None:
                print('\n------ parse next page --------')
                print(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                pass
        else:
            print('========= Last page ==========')
            
            
    def comics_parse(self,response):
        #提取每部漫画数据
        content=response.body
        if not content:
            self.log('parse comics body error')
            return
        
        # 注意BeautifulSoup的解析器参数，不能指定为'html.parser'，因为有些网页可能为 lxml
        soup = BeautifulSoup(content, "html5lib")
        #选择页控件标签
        page_list_tag=soup.find('ul',class_='pagelist')
        #获取当前页数
        current_li=page_list_tag.find('li',class_='thisclass')
        page_num=current_li.a.string
        self.log('curent page='+page_num)
        #获取当前页图片URL，以及漫画标题，

        li_tag=soup.find('li',id='imgshow')
        img_tag=li_tag.find('img')
        #获取当前图片的url
        img_url=img_tag['src']
        self.log('img url: ' + img_url)
        # 漫画标题 
        title=img_tag['alt']
        #将图片保存到本地
        self.save_img(page_num, title, img_url)
        
        # 下一页图片的url，当下一页标签的href属性为‘#’时为漫画的最后一页
        a_tag_list = page_list_tag.find_all('a')
        next_page = a_tag_list[-1]['href']
        if next_page == '#':
            self.log('parse comics:' + title + 'finished.')
        else:
            next_page = 'http://www.xedq8.com/shenshi/' + next_page
            yield scrapy.Request(next_page, callback=self.comics_parse)
        
      
        
    def save_img(self,img_num,title,img_url):
        #将图片保存到本地
        self.log('saving pic:'+img_url)
        #保存图片到文件夹
        document='/Users/chaoyifei/Desktop/cartoon'
        #每个漫画的文件名以标题命名
        photo_patch=document+'/'+title
        #判断文件夹是否存在
        exists=os.path.exists(photo_patch)
        if not exists:
            self.log('create document'+title)
            os.makedirs(photo_patch)
        
        #每张图片以页数命名
        pic_name=photo_patch+'/'+img_num+'.jpg'
        
        #查看图片是否以及下载到本地,若存在则不再重新下载
        
        exists=os.path.exists(pic_name)
        if exists:
            self.log('pic exists:'+pic_name)
            return
        try:
            #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            #headers = { 'User-Agent' : user_agent }
            
            header= {
                     'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',  
                     
        
                        }   
    
 
            #req = urllib.request.Request(img_url, headers=header)
            req = urllib2.Request(img_url, headers=header)
        
            #response = urllib.request.urlopen(req, timeout=40)
            response = urllib2.urlopen(req, timeout=40)
            #请求返回到的数据
            data=response.read()
            #若返回压缩数据则需先解压缩
            if response.info().get('Content-Encoding')=='gzip':
                data=zlib.decompress(data)
            #图片保存到本地
            fp=open(pic_name,'wb')
            fp.write(data)
            fp.close
            self.log('save image finished'+pic_name)
        except Exception as e:
            self.log('save image error')
            self.log(e)
            
            
               
              
        
        
        
        
                
        
        
        
