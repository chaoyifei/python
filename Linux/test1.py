#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/05/26 上午 9:17
@Author  : chaoyifei
@File    : test1.py
@Software: PyCharm
'''

# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx

ID_PXFS = 1000


###########################################################################
## Class MyDialog1
###########################################################################
class MyDialog1(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"照片重命名工具", pos=wx.DefaultPosition, size=wx.Size(607, 354),
                           style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"排序方式:", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ST_NO_AUTORESIZE)
        self.m_staticText1.Wrap(-1)
        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        m_choice2Choices = [u"创建时间", u"修改时间", u"访问时间", u"拍摄时间"]
        self.m_choice2 = wx.Choice(self, ID_PXFS, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        bSizer3.Add(self.m_choice2, 0, wx.ALL, 5)

        m_choice21Choices = [u"升序", u"降序"]
        self.m_choice21 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice21Choices, 0)
        self.m_choice21.SetSelection(0)
        bSizer3.Add(self.m_choice21, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"源文件夹:", wx.DefaultPosition, wx.DefaultSize, 0)

        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择源文件夹", wx.DefaultPosition,
                                             wx.DefaultSize,
                                             wx.DIRP_DEFAULT_STYLE)
        bSizer6.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"目标文件夹:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_dirPicker2 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择目标文件夹", wx.DefaultPosition,
                                             wx.DefaultSize,
                                             wx.DIRP_DEFAULT_STYLE)
        bSizer6.Add(self.m_dirPicker2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"文件名列表:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择文件名列表文件", u".csv",
                                               wx.DefaultPosition,
                                               wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer7.Add(self.m_filePicker1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"重命名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetDefault()
        bSizer8.Add(self.m_button2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"照片重命名工具\n版本:v1.0\n作者:无心问世\n邮箱:lan-yu@139.com\n程序使用方法:\n先选择文件排序方式,然后选择源文件夹(存照片的文件夹),再选择目标文件夹(照片重命名后存放的文件夹),再点击重命名即可",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer9.Add(self.m_staticText5, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer9, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_choice2.Bind(wx.EVT_CHOICE, self.p)
        self.m_choice21.Bind(wx.EVT_CHOICE, self.m)
        self.m_dirPicker1.Bind(wx.EVT_DIRPICKER_CHANGED, self.src_dir)
        self.m_dirPicker2.Bind(wx.EVT_DIRPICKER_CHANGED, self.dst_dir)
        self.m_filePicker1.Bind(wx.EVT_FILEPICKER_CHANGED, self.file_name_list)
        self.m_button2.Bind(wx.EVT_BUTTON, self.start)

    def __del__(self):
        pass
        # Virtual event handlers, overide them in your derived class

    def p(self, event):
        event.Skip()

    def m(self, event):
        event.Skip()

    def src_dir(self):
        src_path = self.m_dirPicker1.GetPath()
        # return src_path
        return src_path

    def dst_dir(self):
        dst_path = self.m_dirPicker2.GetPath()
        return dst_path

    def file_name_list(self):
        file_list = self.m_filePicker1.GetPath()
        return file_list

    def start(self, e):
        src_path = self.src_dir()
        dst_path = self.dst_dir()
        file_list = self.file_name_list()
        self.mk(src_path, dst_path, file_list)
        e.Skip()

    def mk(self, src_path, dst_path, file_list):
        print src_path
        print dst_path
        print file_list


class App(wx.App):
    def OnInit(self):
        frame = MyDialog1(None)
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
