# -*- encoding:UTF-8 -*-
import Base
import wx
from libs import Utility
from libs.Config import String


class DeviceSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name=String.Device, title=u"请选择设备")

    def get_choices(self):
        _type = self._get_value(String.DeviceType)
        if _type == String.Android:
            return Utility.get_adb_devices()
        elif _type == String.Serial:
            return list('321')
        else:
            return ["Unknow"]


if __name__ == '__main__':
    app = wx.App()
    f = DeviceSelection()
    f.Show()
    app.MainLoop()
