# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String
import Base


class DeviceType(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name="device_type")

    def _refresh(self):
        return [String.Android, String.Serial]


if __name__ == "__main__":
    app = wx.App()
    f = DeviceType()
    f.Show()
    app.MainLoop()
