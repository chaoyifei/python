#coding:utf-8
'''
Created on 2017年7月18日

@author: Administrator
'''
#HTMLTestRunner.py来生成自动化测试报告

import HTMLTestRunner
import os
import unittest
import time

#设置报告文件生产路径
report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
#获取系统当前时间
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile=report_path+now+"HTMLtemplate.html" 
fp=file(HtmlFile,"wb")

#构建suite

suite=unittest.TestLoader().discover("testsuit")

if __name__=='__main__':
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"目测试报告",description=u"用例测试情况")
    runner.run(suite)
    