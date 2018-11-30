# -*- encoding:UTF-8 -*-
import wx
from libs.UserInterface.Dialogs.CreateCase import Base
import os
from libs import Utility


class StorageSetting(Base.SettingPage):
    def __init__(self, parent):
        Base.SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        wx_static_text = wx.StaticText(self, wx.ID_ANY, u"请设置测试过程中产生文件的存放路径:", wx.DefaultPosition, wx.DefaultSize, 0)
        main_sizer.Add(wx_static_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        self.dir_picker = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"请选择一个目录：", wx.DefaultPosition,
                                           wx.DefaultSize,
                                           wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL | wx.DIRP_DIR_MUST_EXIST)
        main_sizer.Add(self.dir_picker, 0, wx.EXPAND | wx.ALL, 3)
        self.SetSizer(main_sizer)

    def update(self):
        path = self.dir_picker.GetPath()
        if os.path.exists(path):
            self._set_value('storage', path)
        else:
            Utility.Alert.Error(u"目录不存在：%s" % path)
            raise AttributeError

    def Init(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    f = StorageSetting()
    f.Show()
    app.MainLoop()
