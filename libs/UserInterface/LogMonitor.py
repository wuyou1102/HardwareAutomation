# -*- encoding:UTF-8 -*-
import wx
import logging
from libs.Config import Color
from libs.Config import String
from ObjectListView import ObjectListView, ColumnDefn, Filter
import time

logger = logging.getLogger(__name__)


class LogMonitor(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=title, size=(600, 400))
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.list_view = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        main_sizer.Add(self.list_view, 1, wx.EXPAND | wx.ALL, 1)
        self._name = title
        self.SetSizer(main_sizer)
        self.Layout()

    @property
    def name(self):
        return self._name

    def __set_columns(self):
        self.list_view.SetColumns(
            [
                ColumnDefn(title=u"No.", align="left", width=60, valueGetter='_index'),
                ColumnDefn(title=u"Time", align="left", width=80, valueGetter='_time'),
                ColumnDefn(title=u"Level", align="left", width=40, valueGetter='_level'),
                ColumnDefn(title=u"Message", align="left", width=80, valueGetter='_msg'),
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
        elif item.LEVEL == String.LEVEL_RSLT:
            list_view.SetBackgroundColour(Color.LemonChiffon)
        else:
            list_view.SetBackgroundColour(Color.White)


class LogData(object):
    def __init__(self, index, level, msg):
        self._index = index
        self._time = get
        self._level = level
        self._msg = msg

    @property
    def LEVEL(self):
        return self._level




if __name__ == '__main__':
    app = wx.App()
    f = LogMonitor("hello world")
    f.Show()
    app.MainLoop()
