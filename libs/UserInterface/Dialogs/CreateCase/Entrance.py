# -*- encoding:UTF-8 -*-
import wx
from _1_DevicesType import DeviceType
from _2_DevicesSelection import DeviceSelection
from _3_CaseSelection import CaseSelection


class Entrance(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"创建测试", pos=wx.DefaultPosition,
                           size=(400, 500), style=wx.DEFAULT_DIALOG_STYLE)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.case = dict
        self.pages = [DeviceType]
        self.setting_panel = wx.Panel(self)
        setting_sizer = wx.BoxSizer(wx.VERTICAL)
        self.setting_panel.SetSizer(setting_sizer)
        self.setting_panel.SetBackgroundColour('black')
        self.sizer.Add(self.setting_panel, 1, wx.EXPAND | wx.ALL, 0)
        self.sizer.Add(wx.StaticLine(self, style=wx.LI_HORIZONTAL), 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.__init_btn_sizer(), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
        self.sizer.Fit(self.setting_panel)
        self.SetSizer(self.sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        self.hello_world()
        self.hello_world1()
        self.hello_world1()
        self.hello_world1()
        self.hello_world1()
        self.hello_world1()

    def __init_btn_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_size = (110, -1)
        btn_back = wx.Button(self, wx.ID_ANY, u"< Back", wx.DefaultPosition, btn_size, 0)
        btn_next = wx.Button(self, wx.ID_ANY, u"Next >", wx.DefaultPosition, btn_size, 0)
        btn_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, btn_size, 0)
        btn_back.Bind(wx.EVT_BUTTON, self.on_back)
        btn_next.Bind(wx.EVT_BUTTON, self.on_next)
        btn_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        sizer.Add(btn_back, 1, wx.ALL, 5)
        sizer.Add(btn_next, 1, wx.ALL, 5)
        sizer.Add(btn_cancel, 1, wx.ALL, 5)
        return sizer

    def on_back(self, event):
        pass

    def on_next(self, event):
        pass

    def on_cancel(self, event):
        pass

    def add_setting_page(self):
        pass

    def hello_world(self):

        sizer = self.setting_panel.GetSizer()

        d = DeviceType(self)
        sizer.Add(d, 1, wx.EXPAND | wx.ALL, 0)
        self.setting_panel.SetSizer(sizer)
        self.setting_panel.Layout()
        sizer.Fit(self.setting_panel)
        self.Layout()

    def hello_world1(self):
        # self.setting_panel.GetSizer().Destroy()
        sizer = self.setting_panel.GetSizer()


        d = DeviceSelection(self)
        sizer.Add(d, 1, wx.EXPAND | wx.ALL, 0)
        self.setting_panel.SetSizer(sizer)
        self.setting_panel.Layout()
        sizer.Fit(self.setting_panel)
        self.Layout()

    def get_test_case(self):
        return self.case


if __name__ == '__main__':
    Entrance()
