# -*- encoding:UTF-8 -*-
import wx
from libs.Config import String


class Case(object):
    def __init__(self, parent, _id, **kwargs):
        self._parent = parent
        self._id = _id
        self.panel = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel.SetBackgroundColour("#CAFCFA")
        self._init_variable(**kwargs)
        self._init_test(**kwargs)
        self._init_division()

    def Hide(self):
        self.panel.Hide()

    def _init_variable(self, **kwargs):
        self._device = kwargs.get(String.Device)
        self._device_type = kwargs.get(String.CaseType)
        self._case_name = kwargs.get(String.CaseName)

    def _init_test(self, **kwargs):
        case_class = kwargs.get(String.Case)
        args = case_class.convert_dict_to_tuple(**kwargs)
        self._case = case_class(*args)

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
        self.Pass = wx.StaticText(self.panel, wx.ID_ANY, str(self._id), wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fail = wx.StaticText(self.panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(Pass, 0, wx.ALL, 3)
        sizer.Add(self.Pass, 0, wx.ALL, 3)
        sizer.Add(Fail, 0, wx.ALL, 3)
        sizer.Add(self.Fail, 0, wx.ALL, 3)
        return sizer

    def _init_operation_sizer(self):
        btn_size = (25, 25)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row1 = wx.BoxSizer(wx.HORIZONTAL)
        row2 = wx.BoxSizer(wx.HORIZONTAL)
        start = wx.Button(self.panel, wx.ID_ANY, u"A", wx.DefaultPosition, btn_size, 0)
        pause = wx.Button(self.panel, wx.ID_ANY, u"B", wx.DefaultPosition, btn_size, 0)
        destroy = wx.Button(self.panel, wx.ID_ANY, u"C", wx.DefaultPosition, btn_size, 0)
        destroy.Bind(wx.EVT_BUTTON, self.on_destroy)
        log = wx.Button(self.panel, wx.ID_ANY, u"D", wx.DefaultPosition, btn_size, 0)
        row1.Add(start, 0, wx.ALL, 1)
        row1.Add(pause, 0, wx.ALL, 1)
        row2.Add(destroy, 0, wx.ALL, 1)
        row2.Add(log, 0, wx.ALL, 1)
        sizer.Add(row1, 0, wx.ALL, 1)
        sizer.Add(row2, 0, wx.ALL, 1)
        return sizer

    def _init_division(self):
        self._division = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        case_sizer = self._init_case_sizer()
        device_sizer = self._init_device_sizer()
        result_sizer = self._init_result_sizer()
        right_sizer = self._init_operation_sizer()
        left_sizer.Add(case_sizer, 0, wx.EXPAND | wx.ALL, 0)
        left_sizer.Add(device_sizer, 0, wx.EXPAND | wx.ALL, 0)
        left_sizer.Add(result_sizer, 0, wx.EXPAND | wx.ALL, 0)
        sizer.Add(left_sizer, 1, wx.EXPAND | wx.ALL, 0)
        sizer.Add(right_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        self.panel.SetSizer(sizer)
        self.panel.Layout()
        sizer.Fit(self.panel)
        self._division.Add(self.panel, 1, wx.EXPAND | wx.ALL, 0)

    def get_division(self):
        return self._division

    @property
    def id(self):
        return self._id

    def on_destroy(self, event):
        self.panel.Destroy()
        self._parent.remove_test_division(self._id)

    def stop(self, event):
        self._case.stop()
