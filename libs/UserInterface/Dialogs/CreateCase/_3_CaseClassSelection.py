# -*- encoding:UTF-8 -*-

import Base
import wx
from libs.Config import String
import cases


class CaseClassSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name=String.CaseGroup, need_refresh=False, title=u"请选择测试分类")

    def get_choices(self):
        _type = self._get_value(String.DeviceType)
        dir_class = dir(getattr(cases, _type))
        return [x for x in dir_class if not x.startswith('__') or not x.endswith('__')]


if __name__ == '__main__':
    app = wx.App()
    f = CaseClassSelection()
    f.Show()
    app.MainLoop()
