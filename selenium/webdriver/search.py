#coding=utf-8
'''
Created on 2017年7月15日

@author: Administrator

'''
import time
import unittest
from selenium import webdriver

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        '''
        setup()主要为测试前的准备工作
        '''
        self.driver=webdriver.Ie()
        self.driver.maximize_window()
        #self.implicitly_wait(8)
        self.driver.get("https://www.baidu.com") 
    def tearDown(self):
        '''
                        测试结束后关闭浏览器
        '''
        self.driver.quit()
    def test_baidu_search(self):
        '''
                        测试内容逻辑test开头
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass')
        except Exception as e:
            print('Test Fail.',format(e))
            
            
            
if __name__=='__main__':
    unittest.main()