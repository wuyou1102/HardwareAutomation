# -*- encoding:UTF-8 -*-
import sys
import wx
from libs.UserInterface.Dialogs import CreateCase

reload(sys)
sys.setdefaultencoding('utf-8')


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title="硬件自动化测试", size=(400, 600))
        self.Center()
        self.panel = FramePanel(self)


class FramePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        operation_sizer = self.__init_operation_sizer()
        self.scrolled_window = self.__init_scrolled_window()
        main_sizer.Add(operation_sizer, 0, wx.EXPAND | wx.ALL, 0)
        main_sizer.Fit(self.scrolled_window)
        main_sizer.Add(self.scrolled_window, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(main_sizer)
        self.Layout()

    def __init_scrolled_window(self):
        scrolled_window = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.VSCROLL)
        scrolled_window.SetScrollRate(5, 5)
        scrolled_window.Layout()
        return scrolled_window

    def __init_operation_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        create = wx.Button(self, wx.ID_ANY, u"创建测试", wx.DefaultPosition, wx.DefaultSize, 0)
        create.Bind(wx.EVT_BUTTON, self.__on_create)
        sizer.Add(create, 1, wx.EXPAND | wx.ALL, 5)
        return create

    def __on_create(self, event):
        dlg = CreateCase.Entrance()
        try:
            if dlg.ShowModal() == wx.ID_OK:
                test_case = dlg.get_test_case()
                print test_case
        except UserWarning:
            pass
