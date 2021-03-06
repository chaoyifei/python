#coding:utf-8
'''
Created on 2017年7月16日

@author: Administrator
'''
import sys
import ConfigParser
import os.path
from selenium import webdriver
from logger import Logger



logger = Logger(logger="BrowserEngine").getlog() 

class BrowserEngine():
    dir=os.path.dirname(os.path.abspath('.'))
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    
    def __init__(self,driver):
        self.driver=driver
    
    #打开浏览器
    def open_browser(self,driver):
        config=ConfigParser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'  
        config.read(file_path)
        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")  
        logger.info("The test server url is: %s" % url)  
        #选择浏览器
        if browser == "Firefox":  
            driver = webdriver.Firefox()  
            logger.info("Starting firefox browser.")  
        elif browser == "Chrome":  
            driver = webdriver.Chrome(self.chrome_driver_path)  
            logger.info("Starting Chrome browser.")  
        elif browser == "IE":  
            driver = webdriver.Ie(self.ie_driver_path)  
            logger.info("Starting IE browser.") 
            
        driver.get(url)
        logger.info("open url : %s " %url)
        driver.maximize_window()  
        logger.info("Maximize the current window.")  
        driver.implicitly_wait(10)  
        logger.info("Set implicitly wait 10 seconds.")  
        return driver  
    #关闭浏览器
    def quit_browser(self):  
        logger.info("Now, Close and quit the browser.")  
        self.driver.quit()   