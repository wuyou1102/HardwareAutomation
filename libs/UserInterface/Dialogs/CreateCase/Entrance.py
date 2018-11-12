# -*- encoding:UTF-8 -*-
import wx
import logging
from _1_DevicesType import DeviceType
from _2_DevicesSelection import DeviceSelection
from _3_CaseSelection import CaseSelection

logger = logging.getLogger(__name__)


class Entrance(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"创建测试", pos=wx.DefaultPosition,
                           size=(400, 500), style=wx.DEFAULT_DIALOG_STYLE)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.test_case = dict()
        self.pages = list()
        self.page_index = 0
        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_sizer, 1, wx.EXPAND | wx.ALL, 0)
        self.sizer.Add(wx.StaticLine(self, style=wx.LI_HORIZONTAL), 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.__init_btn_sizer(), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)
        self.SetSizer(self.sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        self.add_page(DeviceType(self))
        self.add_page(CaseSelection(self))
        self.add_page(DeviceSelection(self))

    def __init_btn_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_size = (110, -1)
        btn_back = wx.Button(self, wx.ID_ANY, u"< Back", wx.DefaultPosition, btn_size, 0)
        btn_next = wx.Button(self, wx.ID_ANY, u"Next >", wx.DefaultPosition, btn_size, 0)
        btn_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, btn_size, 0)
        btn_back.Bind(wx.EVT_BUTTON, self.on_back)
        btn_next.Bind(wx.EVT_BUTTON, self.on_next)
        btn_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)
        sizer.Add(btn_back, 1, wx.ALL, 5)
        sizer.Add(btn_next, 1, wx.ALL, 5)
        sizer.Add(btn_cancel, 1, wx.ALL, 5)
        return sizer

    def on_back(self, event):
        self._back()

    def _back(self):
        if self.page_index - 1 != -1:
            self.pages[self.page_index].Hide()
            self.page_index -= 1
            self.pages[self.page_index].Show()
            self.panel_sizer.Layout()
        else:
            print "You're already on the first page!"

    def on_next(self, event):
        self._next()

    def get_current_page(self):
        return self.pages[self.page_index]

    def _next(self):
        if not self.update_test_case():
            return
        if len(self.pages) - 1 != self.page_index:
            self.pages[self.page_index].Hide()
            self.page_index += 1
            self.pages[self.page_index].Show()
            self.panel_sizer.Layout()
        else:
            print "End of pages!"

    def on_cancel(self, event):
        self.Destroy()

    def add_config_page(self):
        pass

    def update_test_case(self):
        try:
            logger.info("BEFORE: %s " % self.test_case)
            page = self.get_current_page()
            page.update()
            logger.info("AFTER: %s " % self.test_case)
            return True
        except NotImplementedError:
            return False
        except AttributeError:
            return False

    def add_page(self, page):
        self.panel_sizer.Add(page, 1, wx.EXPAND | wx.ALL, 0)
        self.pages.append(page)
        if len(self.pages) > 1:
            page.Hide()
            self.Layout()

    def _get_test_case(self):
        return self.test_case


if __name__ == '__main__':
    Entrance()
