# -*- coding:utf-8 -*-
# @Author: CHaoyi
# @Date:   2017-11-06T22:15:07+08:00
# @Filename: Api.py
# @Last modified by:   CHaoyi
# @Last modified time: 2017-11-07T23:29:50+08:00
# 登录App_key和App_secret方式访问微博API
#https://github.com/otakurice/weibonlp

from weibo import APIClient
import webbrowser
import re, time, requests, urllib, request
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

App_key = '2400611080'
App_secret = 'bb9381f9e2cb3e771c5f5449ff8e9ece'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # 回调链接

client = APIClient(app_key=App_key, app_secret=App_secret, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
webbrowser.open_new(url)

print 'please input code '

code = raw_input()
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)
# r = client.comments.show.get(id=4160547165300149, count=200, page=1)
# r1= json.dumps(r,encoding='utf-8',ensure_ascii=False)
# print r1

weibo_id = ('4154417035431509')  # 单条微博ID
url = 'https://m.weibo.cn/api/comments/show?id=' + weibo_id + '&page={}'  # 爬时间排序评论
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Host': 'm.weibo.cn',
    'Accept': 'application/json, text/plain, */*;q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://m.weibo.cn/status/' + weibo_id,
    'Cookie': 'ALF=1512569395; SCF=Am_oMeVmtKxusW2bqPM2Bq2tboM-dQhvoAfmoVm30hFM1YxnCOElOw4yQAduKN_s_57PdgmRBDzA-neEV88QH-U.; SUB=_2A253Bdc-DeRhGeNO6VMT8ybFwzuIHXVUCfl2rDV6PUJbktANLXPBkW1qA44VXJ9g04C0C9ZKqCcDhlEdcw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh6Lb0JMxwuem5b4Kz02AcF5JpX5K-hUgL.Fo-7eo2Ee0n41hM2dJLoI7LhIs8awgLJ9g.t; SUHB=0YhhquN90t0cqa; SSOLoginState=1510057838; _T_WM=47eac210afab7501038eb13a03e0305b; H5:PWA:UID=1; __guid=52195957.3372748557967896000.1510057840112.0652; H5_INDEX=2; H5_INDEX_TITLE=Chaoyifei; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4160547165300149%26luicode%3D20000061%26lfid%3D4160547165300149; monitor_count=16',
    'DNT': '1',
    'Connection': 'keep-alive',
}
i = 0
comment_num = 1
while True:
    r = requests.get(url=url.format(i), headers=headers)
    comment_page = r.json()['data']
    if r.status_code == 200:
        try:
            print('正在读取弟%s页评论：' % i)
            for j in range(0, len(comment_page)):
                print('第%s条评论' % comment_num)
                user = comment_page[j]
                comment_id = user['user']['id']
                # print comment_id
                user_name = user['user']['screen_name']
                # print (user_name)
                created_at = user['created_at']
                # print created_at
                # 屏蔽表情符

                text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]', '', user['text'])
                # print text
                likenum = user['like_counts']
                # print likenum
                source = re.sub('[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]', '', user['source'])
                # print source+'\r\n'
                conn = MySQLdb.connect(host='127.0.0.1', user='root', db='scrpay', passwd='123456', charset='utf8')
                cur = conn.cursor()
                sql = "insert into weibo(comment_id,user_name,created_at,text,likenum,source) values(%s,%s,%s,%s,%s,%s)"
                param = (comment_id, user_name, created_at, text, likenum, source)
                try:
                    A = cur.execute(sql, param)
                    conn.commit()
                    print '成功'
                except Exception as e:
                    print e
                    print '失败'
                    conn.rollback()
                comment_num += 1
            i += 1
            time.sleep(3)
        except Exception as e:
            i += 1
            print e
    else:
        break
