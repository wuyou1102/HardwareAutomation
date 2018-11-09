# -*- encoding:UTF-8 -*-
from Base import SettingPage
import wx


class CaseSelection(SettingPage):
    def __init__(self, parent):
        SettingPage.__init__(self, parent=parent)
        self.test_case = parent.test_case
        self.SetBackgroundColour('red')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.cases = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.__refresh(), 0)
        self.SetSizer(self.sizer)
        self.Layout()

    def __refresh(self):
        return list('abcdefghijkl')


if __name__ == '__main__':
    app = wx.App()
    f = CaseSelection()
    f.Show()
    app.MainLoop()
