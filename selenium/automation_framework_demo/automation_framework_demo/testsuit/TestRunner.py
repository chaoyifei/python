#coding:utf-8
'''
Created on 2017年7月18日
@author: Administrator
'''
#管理测试套
import unittest
import testsuit
from testsuit.baidu_search import BaiduSearch
from testsuit.test_get_page_title import GetPageTitle
suite=unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(GetPageTitle('test_get_title'))


#makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去。

suite=unittest.TestSuite(unittest.makeSuite(BaiduSearch))

#discover（）方法去加载一个路径下所有的测试用例

suite=unittest.TestLoader().discover("testsuit")


if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)