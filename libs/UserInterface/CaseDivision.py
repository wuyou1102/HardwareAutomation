# -*- encoding:UTF-8 -*-
import sys
import wx
from libs.Config import String


class Case(object):
    def __init__(self, parent, **kwargs):
        self._parent = parent
        self.panel = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel.SetBackgroundColour("#CAFCFA")
        self._init_variable(**kwargs)
        self._init_division()

    def _init_variable(self, **kwargs):
        self._device = kwargs.get(String.Device)
        self._device_type = kwargs.get(String.DeviceType)
        self._case_name = kwargs.get(String.CaseName)
        CaseClass = kwargs.get(String.Case)
        args = CaseClass.convert_dict_to_tuple(**kwargs)
        self._case = CaseClass(*args)

    def _init_case_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        case_name = wx.StaticText(self.panel, wx.ID_ANY, self._case_name, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(case_name, 0, wx.ALL, 3)
        return sizer

    def _init_device_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        device = wx.StaticText(self.panel, wx.ID_ANY, self._device, wx.DefaultPosition, wx.DefaultSize, 0)
        type = wx.StaticText(self.panel, wx.ID_ANY, self._device_type, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(type, 0, wx.ALL, 3)
        sizer.Add(device, 0, wx.ALL, 3)
        return sizer

    def _init_result_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        Pass = wx.StaticText(self.panel, wx.ID_ANY, "Pass:", wx.DefaultPosition, wx.DefaultSize, 0)
        Fail = wx.StaticText(self.panel, wx.ID_ANY, "Fail:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Pass = wx.StaticText(self.panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fail = wx.StaticText(self.panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(Pass, 0, wx.ALL, 3)
        sizer.Add(self.Pass, 0, wx.ALL, 3)
        sizer.Add(Fail, 0, wx.ALL, 3)
        sizer.Add(self.Fail, 0, wx.ALL, 3)
        return sizer

    def _init_division(self):
        self._division = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        case_sizer = self._init_case_sizer()
        device_sizer = self._init_device_sizer()
        result_sizer = self._init_result_sizer()
        sizer.Add(case_sizer, 0, wx.EXPAND | wx.ALL, 0)
        sizer.Add(device_sizer, 0, wx.EXPAND | wx.ALL, 0)
        sizer.Add(result_sizer, 0, wx.EXPAND | wx.ALL, 0)
        self.panel.SetSizer(sizer)
        self.panel.Layout()
        sizer.Fit(self.panel)
        self._division.Add(self.panel, 1, wx.EXPAND | wx.ALL, 0)

    def get_division(self):
        return self._division
