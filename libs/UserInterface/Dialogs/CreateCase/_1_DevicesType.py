# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String
from Base import SettingPage


class DeviceType(SettingPage):
    def __init__(self, parent, **kwargs):
        SettingPage.__init__(self, parent=parent)

        button_size = (70, 40)
        self.SetBackgroundColour('red')
        android = wx.Button(self, wx.ID_OK, String.Android, wx.DefaultPosition, button_size, 0)
        serial = wx.Button(self, wx.ID_OK, String.Serial, wx.DefaultPosition, button_size, 0)
        self.sizer.Add(android, 1, wx.ALIGN_CENTER | wx.ALL, 0)
        self.sizer.Add(serial, 1, wx.ALIGN_CENTER | wx.ALL, 0)
        self.SetSizer(self.sizer)
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    f = DeviceType()
    f.Show()
    app.MainLoop()
