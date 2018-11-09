# -*- encoding:UTF-8 -*-
import wx


class SettingPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('Blue')
        self.sizer = wx.BoxSizer(wx.VERTICAL)

    def get_sizer(self):
        return self.sizer
