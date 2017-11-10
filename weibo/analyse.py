# -*- coding:utf-8 -*-
# @Author: CHaoyi
# @Date:   2017-11-09T00:04:40+08:00
# @Filename: analyse.py
# @Last modified by:   CHaoyi
# @Last modified time: 2017-11-11T01:01:09+08:00


import MySQLdb, re, jieba,json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter


# 读取数据库
def readmysql():
    commentlist = []
    textlist = []
    userlist = []
    conn = MySQLdb.connect(host='127.0.0.1', user='root', db='scrpay', passwd='123456', charset='utf8')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM weibo WHERE id < %d' % 13000)
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            del row[0]
            if row not in commentlist:
                commentlist.append(row)
                comment_id = row[0]
                user_name = row[1]
                userlist.append(user_name)
                created_at = row[2]
                text = row[3]
                textlist.append(text)
                likenum = row[4]
                source = row[5]
                #print comment_id.encode('utf-8'),user_name.encode('utf-8'),created_at.encode('utf-8'),text.encode('utf-8'),likenum.encode('utf-8'),source.encode('utf-8')
    return commentlist, textlist, userlist
#云词显示
def wordtocloud(textlist):
    fulltext=''
    cloud = WordCloud(font_path='font.ttf',
            background_color="white",  # 背景颜色
            max_words=2000,  # 词云显示的最大词数
            #mask=back_coloring,  # 设置背景图片
            max_font_size=100,  # 字体最大值
            random_state=42,
            width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
            )
    for li in textlist:
        fulltext += ' '.join(jieba.cut(li,cut_all = False))
    wc = cloud.generate(fulltext)
    #image_colors = ImageColorGenerator(back_coloring)
    plt.figure("wordc")
    plt.imshow(wc.recolor())
    wc.to_file('微博评论词云.png')
if __name__=='__main__':
    commentlist, userlist, textlist=readmysql()

    wordtocloud(textlist)
