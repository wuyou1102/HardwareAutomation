# -*- encoding:UTF-8 -*-
import sys
import wx
from libs.Config import String


class Case(object):
    def __init__(self, parent, **kwargs):
        self._parent = parent
        self.panel = wx.Panel(self._parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel.SetBackgroundColour("#CAFCFA")
        self._init_variable(kwargs)
        self._init_division()

    def _init_variable(self, **kwargs):
        self._device = kwargs.get(String.Device)
        self._device_type = kwargs.get(String.DeviceType)
        self._case_name = kwargs.get(String.CaseName)
        self._case = kwargs.get(String.Case)

    def _init_case_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        return sizer

    def _init_device_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        device = wx.StaticText(self, wx.ID_ANY, self._device, wx.DefaultPosition, wx.DefaultSize, 0)
        type = wx.StaticText(self, wx.ID_ANY, self._device_type, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(type, 0,  wx.ALL, 3)
        sizer.Add(device, 0, wx.ALL, 3)
        return sizer

    def _init_result_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        Pass = wx.StaticText(self, wx.ID_ANY, "Pass:", wx.DefaultPosition, wx.DefaultSize, 0)
        Fail = wx.StaticText(self, wx.ID_ANY, "Fail:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Pass = wx.StaticText(self, wx.ID_ANY, self._device, wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fail = wx.StaticText(self, wx.ID_ANY, self._device_type, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(Pass, 0,  wx.ALL, 3)
        sizer.Add(self.Pass, 0, wx.ALL, 3)
        sizer.Add(Fail, 0, wx.ALL, 3)
        sizer.Add(self.Fail, 0, wx.ALL, 3)
        return sizer

    def _init_division(self):

        self._division = wx.BoxSizer(wx.VERTICAL)
        case_sizer = self._init_case_sizer()
        device_sizer = self._init_device_sizer()
        result_sizer = self._init_result_sizer()

        self._division.Add(case_sizer, 0, wx.EXPAND | wx.ALL, 0)
        self._division.Add(device_sizer, 0, wx.EXPAND | wx.ALL, 0)
        self._division.Add(result_sizer, 0, wx.EXPAND | wx.ALL, 0)
        self.panel.SetSizer(self._division)
        self.panel.Layout()
        self.division.Fit(self.panel)



    def get_division(self):
        return self._division
