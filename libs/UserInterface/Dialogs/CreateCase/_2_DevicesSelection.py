# -*- encoding:UTF-8 -*-
import Base
import wx
from libs.Config import String


class DeviceSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name="device")

    def get_choices(self):
        _type = self._get_value("device_type")
        if _type == String.Android:
            return list('abcdefghijkl')
        elif _type == String.Serial:
            return list('321')
        else:
            return ["Unkown"]


if __name__ == '__main__':
    app = wx.App()
    f = DeviceSelection()
    f.Show()
    app.MainLoop()
