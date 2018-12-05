# -*- encoding:UTF-8 -*-
import wx
from libs.Instrument.SW16 import SW16
from libs.UserInterface.Dialogs.CreateCase import Base


class SW16ButtonSetting(Base.ListSettingPage):
    def __init__(self, parent, attr_name):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name=attr_name)


class SW16DeviceSetting(Base.InstrSettingPage):
    def __init__(self, parent, attr_name):
        Base.InstrSettingPage.__init__(self, parent=parent, attr_name=attr_name)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        wx_static_text = wx.StaticText(self, wx.ID_ANY, u"请选择", wx.DefaultPosition, wx.DefaultSize, 0)
        main_sizer.Add(wx_static_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        self.dir_picker = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"请选择一个目录：", wx.DefaultPosition,
                                           wx.DefaultSize,
                                           wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL | wx.DIRP_DIR_MUST_EXIST)
        main_sizer.Add(self.dir_picker, 0, wx.EXPAND | wx.ALL, 3)
        self.SetSizer(main_sizer)

    def update(self):
        pass

    def get_choices(self):
        return ['sss']


if __name__ == '__main__':
    app = wx.App()
    f = SW16DeviceSetting(parent=None)
    f.Show()
    app.MainLoop()
