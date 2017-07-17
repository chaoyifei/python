#coding:utf-8
'''
Created on 2017年7月16日

@author: Administrator
'''
import time  
import unittest  
from framework.browser_engine import BrowserEngine  
from pageobjects.baidu_homepage import HomePage  

class BaiduSearch(unittest.TestCase):  
  
    '''
    def setUp(self):  
        
        测试固件的setUp()的代码，主要是测试的前提准备工作 
        
        
        browse = BrowserEngine(self)  
        self.driver = browse.open_browser(self)  
    '''
    @classmethod
    def setUpClass(cls):
        browse=BrowserEngine(cls)
        cls.driver=browse.open_browser(cls)
    '''
    def tearDown(self):  
        
                            测试结束后的操作，这里基本上都是关闭浏览器 
         
        
        self.driver.quit()  
    '''
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test_baidu_search(self):  
        '''
                          这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。 
       
        ''' 
        '''
                        注释直接查找，调用封装方法
        self.driver.find_element_by_id('kw').send_keys('selenium')  
        time.sleep(1)  
        '''
        
        #调用页面对象中的方法
        
        homepage=HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()#调用截图类的方法
        
        try:  
            assert 'selenium' in self.driver.title  
            print ('Test Pass.')  
        except Exception as e:  
            print ('Test Fail.', format(e))  
    #添加第二个人测试
    
    def test_search2(self):
        homepage=HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
        
        
        
        
if __name__ == '__main__':  
    unittest.main()  
   
    