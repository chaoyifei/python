#coding=utf-8
import warnings
warnings.filterwarnings("ignore")
import  sys
import jieba
import numpy
import pandas as pd
import urllib2
from bs4 import BeautifulSoup as bs
import re
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud
reload(sys)
sys.setdefaultencoding('utf-8')
#获取源网页

def getNowPlayingMovie_list():
    resq=urllib2.urlopen('https://movie.douban.com/cinema/nowplaying/xian/')
    html_data=resq.read().decode('utf-8')
    #print html_data

    soup=bs(html_data,"html.parser")
    nowplaying_movie=soup.find_all('div',id='nowplaying')
    nowplaying_movie_list=nowplaying_movie[0].find_all('li',class_='list-item')

    nowplaying_list=[]
    for item in nowplaying_movie_list:
        nowplaying_dict={}
        nowplaying_dict['id']=item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name']=tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)

    return nowplaying_list
#print nowplaying_list
#解决字典打印中文显示unicode


#获取评论函数
def getCommentsById(movieId,pageNum):
    eachCommentList=[]
    if pageNum>0:
        start=(pageNum-1)*20
    else:
        return False

    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' + '?' + 'start=' + str(start) + '&limit=20'
    print requrl


    resq=urllib2.urlopen(requrl)
    html_data=resq.read().decode('utf-8')
    soup=bs(html_data,'html.parser')
    comment_div_lits=soup.find_all('div',class_='comment')


    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
    #print eachCommentList

    return repr(eachCommentList).decode("unicode–escape")
#主函数
def main():
    #循环获取第一个电影的前十页评论
    commentList=[]
    NowPlayingMovie_list=getNowPlayingMovie_list()
    for i in range(10):
        num=i+1
        commentList_temp=getCommentsById(NowPlayingMovie_list[0]['id'],num)
        commentList.append(commentList_temp)


    #将列表的数据放在一个字符串中
    comments=''
    for k in range(len(commentList)):
        comments=comments+(str(commentList[k])).strip()
    #print comments

    comments=comments.decode('utf-8')
    comments=re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),comments)
    #print comments
    # #过滤标点符号（正则）
    # pattern=re.compile(r'[\u4e00-\u9fa5]+')
    # filter_data=re.findall(pattern,comments)
    # print filter_data
    # cleaned_comment=''.join(filter_data)
    # print cleaned_comment

    #分析词频，用jieba分词
    segment=jieba.lcut(comments)
    words_df=pd.DataFrame({'segment':segment})
    #print words_df.head()
    #去停用词
    stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding='utf-8')
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
    #print words_df.head()

    #词频统计
    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat=words_stat.reset_index().sort_values(by=['计数'],ascending=False)

    #print words_stat.head()

    #用云词显示
    wordcloud=WordCloud(font_path="simhei.ttf",background_color='white',max_font_size=80)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp=(key,word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud=wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.show()
#主函数
main()




