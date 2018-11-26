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
    def __init__(self, parent, attr_name, style=wx.LB_SINGLE, need_refresh=True, title=""):
        SettingPage.__init__(self, parent=parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        if title:
            self.wx_static_text = wx.StaticText(self, wx.ID_ANY, title, wx.DefaultPosition, wx.DefaultSize, 0)
            main_sizer.Add(self.wx_static_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        self.attr_name = attr_name
        self.wx_list = wx.ListBox(parent=self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                                  choices=[], style=style)
        self.wx_list.Bind(wx.EVT_LISTBOX_DCLICK, self.double_click_on_list)
        main_sizer.Add(self.wx_list, 1, wx.EXPAND | wx.ALL, 3)
        if need_refresh:
            refresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, (-1, 30), 0)
            refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
            main_sizer.Add(refresh, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
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
        if len(items) == 1:
            self.wx_list.SetSelection(0)

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


class IntSettingPage(SettingPage):
    def __init__(self, parent, attr_name, min, max, style=wx.SP_ARROW_KEYS, initial=None, title=""):
        SettingPage.__init__(self, parent=parent)
        initial = initial if initial is not None else min
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        if title:
            title = u'{title}  ({min}～{max})'.format(title=title, min=min, max=max)
            wx_static_text = wx.StaticText(self, wx.ID_ANY, title, wx.DefaultPosition, wx.DefaultSize, 0)
            main_sizer.Add(wx_static_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        self.attr_name = attr_name
        self.wx_spin = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value=wx.EmptyString, pos=wx.DefaultPosition,
                                   size=wx.DefaultSize, style=style, min=min, max=max, initial=initial)
        main_sizer.Add(self.wx_spin, 0, wx.EXPAND | wx.ALL, 3)
        self.SetSizer(main_sizer)

    def update(self):
        attr_value = self.wx_spin.GetValue()
        self._set_value(self.attr_name, attr_value)

    def Init(self):
        pass
