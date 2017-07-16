#coding:utf-8
'''
Created on 2017年7月16日

@author: Administrator
'''
from framework.base_page import BasePage

class HomePage(BasePage):
    
    input_box="id=>kw"
    search_submit_btn="xpath=>//*[@id='su']"
    
    def type_search(self,text):
        self.type(self.input_box,text)
        
    def send_submit_btn(self):
        self.click(self.search_submit_btn)