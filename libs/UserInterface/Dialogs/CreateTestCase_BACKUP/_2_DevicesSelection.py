# -*- encoding:UTF-8 -*-
import Base
import wx
from Base import SettingPage


class DeviceSelection(SettingPage):
    def __init__(self, parent):
        SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        refresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.devices = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.__refresh(), 0)
        main_sizer.Add(self.devices, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(refresh, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        self.SetSizer(main_sizer)

    def __refresh(self):
        return list('abcdefghijkl')


if __name__ == '__main__':
    app = wx.App()
    f = DeviceSelection()
    f.Show()
    app.MainLoop()
