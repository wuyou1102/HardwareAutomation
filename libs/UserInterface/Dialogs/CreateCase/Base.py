# -*- encoding:UTF-8 -*-
import wx
from libs import Utility


class SettingPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

    def _set_value(self, attr_name, attr_value):
        self.parent.test_case[attr_name] = attr_value

    def _get_value(self, attr_name):
        return self.parent.test_case[attr_name]

    def next_page(self):
        self.parent._next()

    def update(self):
        raise NotImplementedError

    def Init(self):
        raise NotImplementedError


class ListSettingPage(SettingPage):
    def __init__(self, parent, attr_name, style=wx.LB_SINGLE, need_refresh=True):
        SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.attr_name = attr_name
        self.wx_list = wx.ListBox(parent=self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                                  choices=[], style=style)
        self.wx_list.Bind(wx.EVT_LISTBOX_DCLICK, self.double_click_on_list)
        if need_refresh:
            button_size = (70, 40)
            refresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, button_size, 0)
            refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
            sizer.Add(refresh, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(self.wx_list, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        self.SetSizer(main_sizer)


    def on_refresh(self, event):
        Utility.append_thread(self._refresh, allow_dupl=False)

    def Init(self):
        Utility.append_thread(self._refresh, allow_dupl=False)

    def _refresh(self):
        self.wx_list.SetItems(['Refresh'])
        self.wx_list.Disable()
        items = self.get_choices()
        self.wx_list.SetItems(items)
        self.wx_list.Enable()

    def get_choices(self):
        raise NotImplementedError

    def update(self):
        attr_value = self.wx_list.GetStringSelection()
        if attr_value:
            self._set_value(self.attr_name, attr_value)
        else:
            Utility.Alert.Error(u"请选择选项")
            raise AttributeError

    def double_click_on_list(self, event):
        self.next_page()
