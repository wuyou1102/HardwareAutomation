# -*- encoding:UTF-8 -*-
from libs.UserInterface.Dialogs.CreateCase import Base
import wx
from libs import Utility
from libs.Config import String


class DeviceSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name='device', title=u"请选择设备")
        self.wx_static_text.SetLabel(self.get_title())

    def get_choices(self):
        _type = self._get_value(String.CaseType)
        if _type == String.Android:
            return Utility.get_adb_devices()
        elif _type == String.Serial:
            return Utility.get_serial_ports()
        else:
            raise KeyError

    def get_title(self):
        _type = self._get_value(String.CaseType)
        if _type == String.Android:
            return u"请选择Android设备"
        elif _type == String.Serial:
            return u"请选择串口设备端口"
        else:
            raise KeyError


if __name__ == '__main__':
    app = wx.App()
    f = DeviceSelection()
    f.Show()
    app.MainLoop()
