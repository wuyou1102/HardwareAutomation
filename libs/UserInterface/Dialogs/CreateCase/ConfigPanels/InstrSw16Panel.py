# -*- encoding:UTF-8 -*-
import wx
from libs.Instrument.SW16 import SW16
from libs.UserInterface.Dialogs.CreateCase import Base
from libs import Utility


class SW16ButtonSetting(Base.ListSettingPage):
    def __init__(self, parent, attr_name):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name=attr_name, need_refresh=False)
        self.wx_static_text.SetLabel(u"选择[%s]的继电器按钮:" % attr_name)

    def get_choices(self):
        instr = self._get_value(u'SW16_device')
        return instr.get_buttons()

    def update(self):
        selection = self.wx_list.GetStringSelection()
        instr = self._get_value(u'SW16_device')
        if selection:
            self._set_value(self.attr_name, instr.get_button(selection))
        else:
            Utility.Alert.Error(u"请选择选项")
            raise AttributeError


class SW16DeviceSetting(Base.InstrSettingPage):
    def __init__(self, parent, attr_name):
        Base.InstrSettingPage.__init__(self, parent=parent, attr_name=attr_name)
        self.wx_static_text.SetLabel(u"请选择要使用的SW16设备：")

    def get_choices(self):
        return SW16.get_instruments()

    def on_create(self, event):
        dlg = SW16CreateDialog()
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            SW16.create(dlg.get_port())
            self.refresh()

    def update(self):
        selection = self.wx_list.GetStringSelection()
        if selection:
            self._set_value(self.attr_name, SW16.get_instrument(selection))
        else:
            Utility.Alert.Error(u"请选择选项")
            raise AttributeError


class SW16CreateDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"初始化SW16设备", pos=wx.DefaultPosition,
                           size=(300, 250), style=wx.DEFAULT_DIALOG_STYLE)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.wx_static_text = wx.StaticText(self, wx.ID_ANY, u"请选择SW16的虚拟端口:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wx_list = wx.ListBox(parent=self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                                  choices=Utility.get_serial_ports(), style=wx.LB_SINGLE)
        main_sizer.Add(self.wx_static_text, 0, wx.EXPAND | wx.ALL, 3)
        main_sizer.Add(self.wx_list, 1, wx.EXPAND | wx.ALL, 3)

        refresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, (-1, 30), 0)
        ok = wx.Button(self, wx.ID_OK, u"确定", size=(-1, 30))
        ok.Bind(wx.EVT_BUTTON, self.on_ok)
        cancel = wx.Button(self, wx.ID_CANCEL, u"取消", size=(-1, 30))
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(ok, 1, wx.ALIGN_CENTER | wx.ALL, 3)
        button_sizer.Add(cancel, 1, wx.ALIGN_CENTER | wx.ALL, 3)
        refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        main_sizer.Add(refresh, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        main_sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(main_sizer)
        self.Center()

    def get_port(self):
        return self.wx_list.GetStringSelection()

    def on_refresh(self, event):
        items = Utility.get_serial_ports()
        self.wx_list.SetItems(items)
        if len(items) == 1:
            self.wx_list.SetSelection(0)

    def on_ok(self, event):
        if not self.wx_list.GetStringSelection():
            Utility.Alert.Error(msg=u"请选择SW16的虚拟端口")
        else:
            event.Skip()


if __name__ == '__main__':
    app = wx.App()
    f = SW16DeviceSetting(parent=None)
    f.Show()
    app.MainLoop()
