# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String
from Base import SettingPage


class DeviceType(SettingPage):
    def __init__(self, parent):
        SettingPage.__init__(self, parent=parent)
        self.test_case = parent.test_case
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._type = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, [String.Android, String.Serial], 0)
        self._type.SetSelection(0)
        sizer.Add(self._type, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        self.Layout()

    def set_value(self):
        value = self._type.GetStringSelection()
        if value:
            self.test_case['device_type'] = self._type.GetStringSelection()
            return True
        return False


if __name__ == "__main__":
    app = wx.App()
    f = DeviceType()
    f.Show()
    app.MainLoop()
