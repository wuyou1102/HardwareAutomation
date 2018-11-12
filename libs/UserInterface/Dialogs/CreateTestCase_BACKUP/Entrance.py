# -*- encoding:UTF-8 -*-
import wx
from _1_DevicesType import DeviceType
from _2_DevicesSelection import DeviceSelection
from _3_CaseSelection import CaseSelection
from wx.adv import *


class Entrance(Wizard):
    def __init__(self, parent):
        Wizard.__init__(self, parent=parent, id=wx.ID_ANY, title=wx.EmptyString, bitmap=wx.NullBitmap,
                        pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.test_case = dict()
        self.pages = list()
        self.add_page(DeviceType(self))
        self.add_page(DeviceSelection(self))
        self.add_page(CaseSelection(self))
        self.Bind(EVT_WIZARD_BEFORE_PAGE_CHANGED, self.BEFORE_PAGE_CHANGED)
        self.Centre(wx.BOTH)

    def add_page(self, page):
        if self.pages:
            previous_page = self.pages[-1]
            page.SetPrev(previous_page)
            previous_page.SetNext(page)
        self.pages.append(page)

    def BEFORE_PAGE_CHANGED(self, event):
        page = self.GetCurrentPage()
        if page.set_value():
            print self.test_case

    def run(self):
        self.RunWizard(self.pages[0])


if __name__ == '__main__':
    Entrance()
