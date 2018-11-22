# -*- encoding:UTF-8 -*-
import wx

from libs.Config import String
from libs import Utility


class Case(object):
    def __init__(self, parent, _id, **kwargs):
        self._parent = parent
        self._id = _id
        self._short_id = _id[-6:]
        self._panel = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self._panel.SetBackgroundColour("#33DDFF")
        self._init_variable(**kwargs)
        self._init_test(**kwargs)
        self._init_division()
        self.stop_flag = False

    def _init_variable(self, **kwargs):
        self._loop = kwargs.get(String.CaseLoop)
        self._case_type = kwargs.get(String.CaseType)
        self._case_name = kwargs.get(String.CaseName)

    def _init_test(self, **kwargs):
        case_class = kwargs.get(String.Case)
        args = case_class.convert_dict_to_tuple(**kwargs)
        self._case = case_class(*args)

    def _init_case_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        case_name = wx.StaticText(self._panel, wx.ID_ANY, self._case_name, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(case_name, 0, wx.ALL, 3)
        return sizer

    def _init_device_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        type = wx.StaticText(self._panel, wx.ID_ANY, self._case_type, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(type, 0, wx.ALL, 3)
        return sizer

    def _init_result_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        wx_pass = wx.StaticText(self._panel, wx.ID_ANY, u"成功:", wx.DefaultPosition, wx.DefaultSize, 0)
        wx_fail = wx.StaticText(self._panel, wx.ID_ANY, u"失败:", wx.DefaultPosition, wx.DefaultSize, 0)
        wx_error = wx.StaticText(self._panel, wx.ID_ANY, u"异常:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wx_pass = wx.StaticText(self._panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wx_fail = wx.StaticText(self._panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wx_error = wx.StaticText(self._panel, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(wx_pass, 0, wx.ALL, 3)
        sizer.Add(self.wx_pass, 0, wx.ALL, 3)
        sizer.Add(wx_fail, 0, wx.ALL, 3)
        sizer.Add(self.wx_fail, 0, wx.ALL, 3)
        sizer.Add(wx_error, 0, wx.ALL, 3)
        sizer.Add(self.wx_error, 0, wx.ALL, 3)
        return sizer

    def _init_operation_sizer(self):
        btn_size = (25, 25)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row1 = wx.BoxSizer(wx.HORIZONTAL)
        row2 = wx.BoxSizer(wx.HORIZONTAL)
        start = wx.Button(self._panel, wx.ID_ANY, u">", wx.DefaultPosition, btn_size, 0)
        stop = wx.Button(self._panel, wx.ID_ANY, u"█", wx.DefaultPosition, btn_size, 0)
        destroy = wx.Button(self._panel, wx.ID_ANY, u"C", wx.DefaultPosition, btn_size, 0)
        log = wx.Button(self._panel, wx.ID_ANY, u"D", wx.DefaultPosition, btn_size, 0)
        start.Bind(wx.EVT_BUTTON, self.on_start)
        stop.Bind(wx.EVT_BUTTON, self.on_stop)
        log.Bind(wx.EVT_BUTTON, self.on_log)
        destroy.Bind(wx.EVT_BUTTON, self.on_destroy)
        row1.Add(start, 0, wx.ALL, 1)
        row1.Add(stop, 0, wx.ALL, 1)
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
        self._panel.SetSizer(sizer)
        self._panel.Layout()
        sizer.Fit(self._panel)
        self._division.Add(self._panel, 1, wx.EXPAND | wx.ALL, 0)

    def get_division(self):
        return self._division

    @property
    def division_name(self):
        return u'{id} {case_type} {case_name}'.format(id=self._short_id, case_type=self._case_type,
                                                      case_name=self._case_name)

    @property
    def id(self):
        return self._id

    def on_destroy(self, event):
        if self.is_test_alive():
            Utility.Alert.Error(msg=u"正请先停止正在执行的测试。", title=self.division_name)
            return
        self._panel.Destroy()
        self._parent.remove_test_division(self._id)

    def __stop_test(self):
        if not self.is_test_alive():
            Utility.Alert.Error(u"没有正在执行的测试")
            return
        self.stop_flag = True

    def __start_test(self):
        if self.is_test_alive():
            Utility.Alert.Error(u"测试正在执行中")
            return
        Utility.append_thread(self.__test_execution, thread_name=self._id)

    def on_stop(self, event):
        Utility.Alert.Info(msg=u"正在停止中，请耐心等待。", title=self.division_name)
        self.__stop_test()

    def on_start(self, event):
        self.__start_test()

    def is_test_alive(self):
        return Utility.is_alive(self._id)

    def on_log(self, event):
        pass

    def __test_execution(self):
        self.stop_flag = False
        result = ResultData(self.wx_pass, self.wx_fail, self.wx_error)
        try:
            if self._loop == 0:
                while True:
                    result.Record(self.test_process())
            else:
                for x in xrange(self._loop):
                    result.Record(self.test_process())
            Utility.Alert.Info(msg=u"测试已完成。", title=self.division_name)
        except StopIteration:
            Utility.Alert.Info(msg=u"测试已停止。", title=self.division_name)
        finally:
            pass

    def test_process(self):
        if self.stop_flag:
            raise StopIteration
        return self._case.run()

    def SetBackgroundColour(self, color_hex):
        self._panel.SetBackgroundColour(color_hex)
        self._panel.Layout()
        self._parent.Layout()


class ResultData(object):
    def __init__(self, wx_pass, wx_fail, wx_error):
        self.wx_pass = wx_pass
        self.wx_fail = wx_fail
        self.wx_error = wx_error
        self._pass = 0
        self._fail = 0
        self._error = 0
        self._total = 0
        self.__switch = {
            String.Fail: self.__fail,
            String.Pass: self.__pass,
            String.Error: self.__error,
        }

    def Record(self, result):
        self.__switch[result]()

    @property
    def Pass(self):
        return self._pass

    @property
    def Fail(self):
        return self._fail

    @property
    def Error(self):
        return self._error

    @property
    def Total(self):
        return self._total

    def __pass(self):
        self._pass += 1
        self._total += 1
        self.wx_pass.SetLabel(str(self._pass))

    def __fail(self):
        self._fail += 1
        self._total += 1
        self.wx_fail.SetLabel(str(self._fail))

    def __error(self):
        self._error += 1
        self._total += 1
        self.wx_error.SetLabel(str(self._error))
