# -*- encoding:UTF-8 -*-
import wx
import logging
from libs.Config import Color
from libs.Config import String
from ObjectListView import FastObjectListView, ColumnDefn, Filter
from libs import Utility

logger = logging.getLogger(__name__)


class LogMonitor(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title='', size=(600, 400))
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.__filters = [String.LEVEL_INFO, String.LEVEL_WARM, String.LEVEL_ERROR, String.LEVEL_RESULT]
        filter_sizer = self.__init_filter_sizer()

        self.list_view = FastObjectListView(
            self, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES | wx.SUNKEN_BORDER | wx.LC_NO_SORT_HEADER)
        main_sizer.Add(filter_sizer, 0, wx.EXPAND | wx.ALL, 1)
        main_sizer.Add(self.list_view, 1, wx.EXPAND | wx.ALL, 1)
        self.SetSizer(main_sizer)
        self.Layout()
        self.__set_columns()
        self.__set_row_formatter()
        self.__set_filter()
        self.__logs = list()
        self.__tmp_logs = list()
        self.__timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.AppendLogs, self.__timer)
        self.__timer.Start(500)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def __init_filter_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        def init_checkbox(level):
            wx_checkbox = wx.CheckBox(self, wx.ID_ANY, level, wx.DefaultPosition, wx.DefaultSize, 0, name=level)
            wx_checkbox.Bind(wx.EVT_CHECKBOX, self.set_filter)
            if level in self.__filters:
                wx_checkbox.SetValue(True)
            return wx_checkbox

        sizer.Add(init_checkbox(String.LEVEL_DEBUG), 0, wx.ALL, 5)
        sizer.Add(init_checkbox(String.LEVEL_INFO), 0, wx.ALL, 5)
        sizer.Add(init_checkbox(String.LEVEL_WARM), 0, wx.ALL, 5)
        sizer.Add(init_checkbox(String.LEVEL_ERROR), 0, wx.ALL, 5)
        sizer.Add(init_checkbox(String.LEVEL_RESULT), 0, wx.ALL, 5)
        return sizer

    def set_filter(self, event):
        object = event.GetEventObject()
        if object.IsChecked():
            self.__filters.append(object.GetName())
        else:
            self.__filters.remove(object.GetName())
        self.__set_filter()

    def __set_filter(self):
        _filter = Filter.Chain(Filter.Predicate(lambda item: item._level in self.__filters))
        self.list_view.SetFilter(Filter.Chain(_filter))
        self.list_view.RepopulateList()

    def Info(self, index, msg):
        self.__append_log(LogData(runs=index, level=String.LEVEL_INFO, msg=msg))

    def Error(self, index, msg):
        self.__append_log(LogData(runs=index, level=String.LEVEL_ERROR, msg=msg))

    def Result(self, index, msg):
        self.__append_log(LogData(runs=index, level=String.LEVEL_RESULT, msg=msg))

    def Warm(self, index, msg):
        self.__append_log(LogData(runs=index, level=String.LEVEL_WARM, msg=msg))

    def Debug(self, index, msg):
        self.__append_log(LogData(runs=index, level=String.LEVEL_DEBUG, msg=msg))

    def __append_log(self, log):
        self.__logs.append(log)
        self.__tmp_logs.append(log)

    def AppendLogs(self, event):
        if self.__tmp_logs:
            self.list_view.AddObjects(self.__tmp_logs)
            self.__tmp_logs = []

    def __set_columns(self):
        self.list_view.SetColumns(
            [
                ColumnDefn(title=u"", align="right", width=0, valueGetter=''),
                ColumnDefn(title=u"Runs", align="right", width=70, valueGetter='_runs'),
                ColumnDefn(title=u"Time", align="center", width=100, valueGetter='_time'),
                ColumnDefn(title=u"Level", align="center", width=70, valueGetter='_level'),
                ColumnDefn(title=u"Message", align="left", minimumWidth=150, valueGetter='_msg',
                           isSpaceFilling=True),
            ]
        )

    def __set_row_formatter(self):
        self.list_view.rowFormatter = self.row_formatter

    @staticmethod
    def row_formatter(list_view, item):
        if item.LEVEL == String.LEVEL_INFO:
            list_view.SetBackgroundColour(Color.LightGoldenrodYellow)
        elif item.LEVEL == String.LEVEL_DEBUG:
            list_view.SetBackgroundColour(Color.DarkGray)
        elif item.LEVEL == String.LEVEL_WARM:
            list_view.SetBackgroundColour(Color.Coral)
        elif item.LEVEL == String.LEVEL_ERROR:
            list_view.SetBackgroundColour(Color.OrangeRed)
        elif item.LEVEL == String.LEVEL_RESULT:
            list_view.SetBackgroundColour(Color.LightCyan)
        else:
            list_view.SetBackgroundColour(Color.White)

    def on_close(self, event):
        if self.IsShown():
            self.Show(show=False)
        return True

    def Destroy(self):
        self.__timer.Stop()
        return super(wx.Frame, self).Destroy()


class LogData(object):
    def __init__(self, runs, level, msg):
        self._runs = runs
        self._time = Utility.get_timestamp(time_fmt='%m/%d %H:%M:%S')
        self._level = level
        self._msg = msg

    @property
    def LEVEL(self):
        return self._level

    @property
    def LINE(self):
        return "<{runs}>{timestamp}  {level}: {msg}\n".format(runs=self._runs, timestamp=self._time,
                                                              level=self._level, msg=self._msg)
