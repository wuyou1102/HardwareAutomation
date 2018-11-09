# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String
from Base import SettingPage


class DeviceType(SettingPage):
    def __init__(self, parent):
        SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.__type = None
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_size = (70, 40)
        android = wx.Button(self, wx.ID_OK, String.Android, wx.DefaultPosition, button_size, 0)
        serial = wx.Button(self, wx.ID_OK, String.Serial, wx.DefaultPosition, button_size, 0)
        android.Bind(wx.EVT_BUTTON, self.on_select)
        serial.Bind(wx.EVT_BUTTON, self.on_select)
        sizer.Add(android, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        sizer.Add(serial, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        main_sizer.Add(sizer, 1, wx.ALIGN_CENTER | wx.ALL, 0)
        self.SetSizer(main_sizer)
        self.Layout()

    def on_select(self, event):
        obj = event.GetEventObject()
        self.__type = obj.GetLabel()



if __name__ == "__main__":
    app = wx.App()
    f = DeviceType()
    f.Show()
    app.MainLoop()
