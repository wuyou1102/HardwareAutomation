# -*- encoding:UTF-8 -*-
import wx


class SettingPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('Red')
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Fit(self)
        self.sizer.Add(self, 1, wx.EXPAND | wx.ALL, 0)
