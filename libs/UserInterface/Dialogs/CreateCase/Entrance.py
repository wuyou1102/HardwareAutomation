# -*- encoding:UTF-8 -*-
import wx
from _1_DevicesType import DeviceType
from _2_DevicesSelection import DeviceSelection
from _3_CaseSelection import CaseSelection


class Entrance(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=wx.EmptyString, bitmap=wx.NullBitmap,
                        pos=wx.DefaultPosition,style=wx.DEFAULT_DIALOG_STYLE)
        default_size = (400, 300)
        self.setting_page = list
        self.setting_page.add
        self.SetSizeHints(default_size)
        self.Center()
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def add_page(self, page):
        if self.setting_page:
            previous_page = self.setting_page[-1]
            page.SetPrev(previous_page)
            previous_page.SetNext(page)
        self.setting_page.append(page)

    def on_close(self, event):
        self.Destroy()
        return {}


if __name__ == '__main__':
    Entrance()
