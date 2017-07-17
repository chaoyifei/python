#coding:utf-8
'''
Created on 2017年7月17日

@author: Administrator
'''
from framework.base_page import BasePage
class SportNewsHomePage(BasePage):
    #NBA入口
    nba_link="xpath=>//*[@id='channel-submenu']/div/span[2]/a[1]"
    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
        
        
        