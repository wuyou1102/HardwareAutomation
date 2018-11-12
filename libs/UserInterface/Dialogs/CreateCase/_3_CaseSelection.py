# -*- encoding:UTF-8 -*-
import wx
from Base import SettingPage


class CaseSelection(SettingPage):
    def __init__(self, parent):
        SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_size = (70, 40)
        self.SetBackgroundColour("yellow")
        refresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, button_size, 0)
        refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.cases = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.__refresh(), 0)
        sizer.Add(refresh, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        main_sizer.Add(self.cases, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        self.SetSizer(main_sizer)


    def on_refresh(self, event):
        pass

    def get_case(self):
        return self.cases.GetStringSelection()

    def __refresh(self):
        return list('abcdefghijkl')


if __name__ == '__main__':
    app = wx.App()
    f = CaseSelection()
    f.Show()
    app.MainLoop()
