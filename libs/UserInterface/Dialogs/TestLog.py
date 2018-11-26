# -*- encoding:UTF-8 -*-
import wx
import logging

logger = logging.getLogger(__name__)


class Dialog(wx.Dialog):
    def __init__(self, title):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=(600, 300), style=wx.DEFAULT_DIALOG_STYLE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.wx_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, '', style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        sizer.Add(self.wx_text_ctrl, 1, wx.EXPAND | wx.ALL, 2)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def output(self, msg):
        if not msg.endswith('\n'):
            msg = msg + '\n'
        wx.CallAfter(self.wx_text_ctrl.AppendText, text=msg)
