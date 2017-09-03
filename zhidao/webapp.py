#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/01 下午 23:05
@Author  : chaoyifei
@File    : webapp.py
@Software: PyCharm
注：
超轻量级web框架
'''
import web
#路由
url=(
    '/','Index',
    '/test','Test',
    '/question/(\d+).html','Question',
    '/reg','Reg',
    '/login','Login'

)
#连接数据库
db=web.database(dbn='mysql',host='mysql.litianqiang.com',port=7150,user='question',pw='qiangzi()',db='question',charset='utf8')#链接数据库

render=web.template.render('templates')

app=web.application(url,globals())
class Test:
    def  GET(self):#方法名字是用户请求的方式
    #处理业务逻辑
        return '你好'
class Index:
    def GET(self):
        data=db.query("select * from question ORDER BY rand() limit 10")
        return render.index(render.head(),data)
class Question:
    def GET(self,id):
        data=db.query("select * from question WHERE id=%s" %id)
        return render.question(render.head(),data[0])
#注册
class Reg:
    def GET(self):
        return render.reg(render.head())
    def POST(self):
        i=web.input()#获取用户请求数据
        username=i.get('username')
        passwd=i.get('passwd')
        passwd1=i.get('passwd1')
        tel=i.get('tel')
        if not username or not passwd or not passwd1:
             return render.head('请输入完整再提交')
        data=db.query("select * from user WHERE username='%s'" %username)
        if data:
            return render.head('账号已经被注册，请重新输入')
        if passwd!=passwd1:
             return render.head('两次密码不一致')
        db.query("insert into USER (username,passwd,tel) VALUES ('%s','%s','%s')" %(username,passwd,tel))
        return render.head('注册成功')
#登录
class Login:
    def GET(self):
        return render.login(render.head())
    def POST(self):
        i=web.input()
        username=i.get('username')
        passwd=i.get('passwd')
        data=db.query("select * from WHERE usename='%s' and passwd='%s'"%(username,passwd))
        if data:
            return render.head('登录成功')
        else:
            return render.head('账号或密码错误')







if __name__=='__main__':
    app.run()
