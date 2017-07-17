#coding:utf-8
'''
Created on 2017年7月17日

@author: Administrator
'''
from framework.base_page import BasePage
class NewsHomePage(BasePage):
    #点击体育新闻入口
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[5]/a" 

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
        
        
    
    