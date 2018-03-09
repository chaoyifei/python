#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/03/09 下午 20:11
@Author  : chaoyifei
@File    : auto_load.py
@Software: PyCharm
'''
from pywinauto import application
from pywinauto import clipboard
import SendKeys
import win32api
import win32con
import os, sys, time


# 二次封装的类
class Pywin(object):
    # =======================
    # pywin framwork main class
    # =======================

    SLEEP_TIME = 1

    # 初始化方法,初始化一个app
    def __init__(self):
        self.app = application.Application()

    # 启动应用程序
    def run(self, tool_name):
        self.app.start(tool_name)
        time.sleep(self.SLEEP_TIME)

    # 连接应用程序
    def connect(self, tool_name):
        self.app.connect(tool_name)
        time.sleep(self.SLEEP_TIME)

    # 关闭应用程序
    def close(self, tool_name):
        window_name = tool_name.decode('utf - 8')
        self.app[tool_name].Close()

    # 最大化窗口
    def max_window(self, window_name):
        window_name = window_name.decode('utf - 8')
        self.app[window_name].Maximize()
        time.sleep(self.SLEEP_TIME)

    # 菜单点击
    def menu_click(self, window_name,menulist):
        window_name = window_name.decode('utf - 8')
        menulist = menulist.decode('utf - 8')
        self.app[window_name].MenuSelect(menulist)
        time.sleep(self.SLEEP_TIME)

    # 输入内容
    def input(self, window_name, controller, content):
        window_name = window_name.decode('utf - 8')
        controller = controller.decode('utf - 8')
        content = content.decode('utf - 8')
        self.app[window_name][controller].TypeKeys(content)
        time.sleep(self.SLEEP_TIME)

    # 鼠标左键点击
    def click(self, window_name, controller, x=0,y = 0):
        window_name = window_name.decode('utf - 8')
        controller = controller.decode('utf - 8')
        self.app[window_name][controller].Click(button="left", pressed="", coords=(x, y))
        time.sleep(self.SLEEP_TIME)


# 鼠标左键点击(双击)
def double_click(self, window_name, controller, x=0,y = 0):
    window_name = window_name.decode('utf - 8')
    controller = controller.decode('utf - 8')
    self.app[window_name][controller].DoubleClick(button="left", pressed="", coords=(x, y))
    time.sleep(self.SLEEP_TIME)


# 鼠标右键点击,菜单选择
def right_click(self, window_name, controller, order):
    window_name = window_name.decode('utf - 8')
    controller = controller.decode('utf - 8')
    self.app[window_name][controller].RightClick()
    for down in range(order):
        SendKeys.SendKeys('{DOWN}')
        time.sleep(0.5)
    SendKeys.SendKeys('{ENTER}')
    time.sleep(self.SLEEP_TIME)


# 获取剪切板内容
def getclipboard(self):
    return clipboard.GetData(format=13)


# 使用win32点击屏幕
def win32_left_click(self, (x, y), times):
    for count in range(times):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVqENTF_LEFTDOWN, 0, 0, 0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0,0)
        time.sleep(self.SLEEP_TIME)


# 使用win32点击屏幕
def win32_right_click(self, (x, y), times):
    for count in range(times):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVqENTF_RIGHTDOWN, 0, 0, 0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0,0)
        time.sleep(self.SLEEP_TIME)

if __name__ ==  '__main__':

    app = Pywin()
    app.run('notepad.exe')