# -*- encoding:UTF-8 -*-
import wx


class DialogWindow(wx.Dialog):
    def __init__(self, size, name):
        wx.Dialog.__init__(self, None, id=wx.ID_ANY, title=name, pos=wx.DefaultPosition, size=size,
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
