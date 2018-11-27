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
        self.list_view = FastObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        main_sizer.Add(self.list_view, 1, wx.EXPAND | wx.ALL, 1)
        self.SetSizer(main_sizer)
        self.Layout()
        self.__set_columns()
        self.__set_row_formatter()
        self.__logs = list()
        self.__tmp_logs = list()
        self.__timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.AppendLogs, self.__timer)
        self.__timer.Start(500)

    def Info(self, index, msg):
        self.__append_log(LogData(index=index, level=String.LEVEL_INFO, msg=msg))

    def Error(self, index, msg):
        self.__append_log(LogData(index=index, level=String.LEVEL_ERROR, msg=msg))

    def Result(self, index, msg):
        self.__append_log(LogData(index=index, level=String.LEVEL_RESULT, msg=msg))

    def Warm(self, index, msg):
        self.__append_log(LogData(index=index, level=String.LEVEL_WARM, msg=msg))

    def Debug(self, index, msg):
        self.__append_log(LogData(index=index, level=String.LEVEL_DEBUG, msg=msg))

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
                ColumnDefn(title=u"No.", align="left", width=80, valueGetter='_index', isEditable=False),
                ColumnDefn(title=u"Level", align="center", width=60, valueGetter='_level', isEditable=False),
                ColumnDefn(title=u"Time", align="center", width=80, valueGetter='_time', isEditable=False),
                ColumnDefn(title=u"Message", align="left", width=2000, valueGetter='_msg', isEditable=False),
            ]
        )

    def __set_row_formatter(self):
        self.list_view.rowFormatter = self.row_formatter

    @staticmethod
    def row_formatter(list_view, item):
        if item.LEVEL == String.LEVEL_INFO:
            list_view.SetBackgroundColour(Color.White)
        elif item.LEVEL == String.LEVEL_DEBUG:
            list_view.SetBackgroundColour(Color.DoderBlue)
        elif item.LEVEL == String.LEVEL_WARM:
            list_view.SetBackgroundColour(Color.Orange)
        elif item.LEVEL == String.LEVEL_ERROR:
            list_view.SetBackgroundColour(Color.LightCyan)
        elif item.LEVEL == String.LEVEL_RESULT:
            list_view.SetBackgroundColour(Color.LemonChiffon)
        else:
            list_view.SetBackgroundColour(Color.White)

    def Destroy(self):
        if self.IsShown():
            self.Show(show=False)
        return True


class LogData(object):
    def __init__(self, index, level, msg):
        self._index = index
        self._time = Utility.get_timestamp()
        self._level = level
        self._msg = msg

    @property
    def LEVEL(self):
        return self._level

    @property
    def LINE(self):
        return "<{index}>{timestamp}  {level}: {msg}\n".format(index=self._index, timestamp=self._time,
                                                               level=self._level, msg=self._msg)


if __name__ == '__main__':
    app = wx.App()
    f = LogMonitor()
    import threading

    for x in range(1999):
        f.Debug(1, 'ello')
        f.Info(1, 'ello')
        f.Result(1, 'ello')
        f.Error(1, 'ello')

    f.Show()
    app.MainLoop()
