# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String
import Base


class CaseType(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name=String.CaseType, need_refresh=False,
                                      title=u"请选择设备类型")

    def get_choices(self):
        return [String.Android, String.Serial]


if __name__ == "__main__":
    app = wx.App()
    f = CaseType()
    f.Show()
    app.MainLoop()
