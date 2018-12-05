# -*- encoding:UTF-8 -*-
from libs.UserInterface.Dialogs.CreateCase import Base
import wx


class IpAddressSetting(Base.SettingPage):
    def __init__(self, parent, attr_name):
        Base.SettingPage.__init__(self, parent=parent, attr_name=attr_name)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        wx_static_text = wx.StaticText(self, wx.ID_ANY, u"请设置Ip地址:", wx.DefaultPosition, wx.DefaultSize, 0)
        main_sizer.Add(wx_static_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        ip_sizer = wx.BoxSizer(wx.HORIZONTAL)
        spin_size = (60, -1)
        self.wx_spin1 = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value=wx.EmptyString, pos=wx.DefaultPosition,
                                    size=spin_size, min=0, max=255, initial=192)
        self.wx_spin2 = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value=wx.EmptyString, pos=wx.DefaultPosition,
                                    size=spin_size, min=0, max=255, initial=168)
        self.wx_spin3 = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value=wx.EmptyString, pos=wx.DefaultPosition,
                                    size=spin_size, min=0, max=255, initial=1)
        self.wx_spin4 = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value=wx.EmptyString, pos=wx.DefaultPosition,
                                    size=spin_size, min=0, max=255, initial=1)
        ip_sizer.Add(self.wx_spin1, 0, wx.ALIGN_CENTER | wx.ALL, 1)
        ip_sizer.Add(self.wx_spin2, 0, wx.ALIGN_CENTER | wx.ALL, 1)
        ip_sizer.Add(self.wx_spin3, 0, wx.ALIGN_CENTER | wx.ALL, 1)
        ip_sizer.Add(self.wx_spin4, 0, wx.ALIGN_CENTER | wx.ALL, 1)
        main_sizer.Add(ip_sizer, 0, wx.EXPAND | wx.ALL, 3)
        self.SetSizer(main_sizer)

    def update(self):
        attr_value = '%s.%s.%s.%s' % (
            self.wx_spin1.GetValue(),
            self.wx_spin2.GetValue(),
            self.wx_spin3.GetValue(),
            self.wx_spin4.GetValue(),
        )
        self._set_value(self.attr_name, attr_value)

    def Init(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    f = IpAddressSetting()
    f.Show()
    app.MainLoop()
