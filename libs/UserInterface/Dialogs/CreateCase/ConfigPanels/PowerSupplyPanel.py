# -*- encoding:UTF-8 -*-
from libs.UserInterface.Dialogs.CreateCase import Base
import wx
from libs import Utility


class InstrumentSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name='power_supply', title=u"请选择程控电源端口号", need_refresh=True)

    def get_choices(self):
        return Utility.get_visa_resources()


if __name__ == '__main__':
    app = wx.App()
    f = InstrumentSelection()
    f.Show()
    app.MainLoop()
