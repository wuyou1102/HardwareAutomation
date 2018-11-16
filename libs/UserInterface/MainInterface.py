# -*- encoding:UTF-8 -*-
import sys
import wx
from libs.UserInterface.Dialogs import CreateCase
from CaseDivision import Case
import logging
from libs import Utility

logger = logging.getLogger(__name__)
reload(sys)
sys.setdefaultencoding('utf-8')


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"硬件自动化测试", size=(400, 600))
        self.Center()
        self.panel = FramePanel(self)


class FramePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self._init_variable()
        self._parent = parent
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        operation_sizer = self.__init_operation_sizer()
        main_sizer.Add(operation_sizer, 0, wx.EXPAND | wx.ALL, 0)
        # TODO 操作按钮区域,设计预期有 导入导出和创建测试用例功能,目前仅实现创建用例功能
        self.scrolled_sizer = self.__init_scrolled_window()
        main_sizer.Add(self.scrolled_sizer, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(main_sizer)
        self.Layout()

    def _init_variable(self):
        self.test_container = wx.BoxSizer(wx.VERTICAL)  # 创建一个测试展示的容器，所有测试DIV均包含在这个容器内

    def __init_scrolled_window(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.scrolled_window = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL)
        self.scrolled_window.SetScrollRate(5, 5)
        self.scrolled_window.Layout()
        sizer.Fit(self.scrolled_window)
        sizer.Add(self.scrolled_window, 1, wx.EXPAND | wx.ALL, 0)
        return sizer

    def __init_operation_sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        create = wx.Button(self, wx.ID_ANY, u"创建测试", wx.DefaultPosition, wx.DefaultSize, 0)
        create.Bind(wx.EVT_BUTTON, self.__on_create)
        sizer.Add(create, 1, wx.EXPAND | wx.ALL, 5)
        return create

    def __on_create(self, event):
        dlg = CreateCase.Entrance()
        dlg.ShowModal()
        test_case = dlg.get_test_case()
        if test_case is not None:
            logger.info('I got a new test case: ' % test_case)
            self.add_test_division(test_case=test_case)
            self.refresh_scrolled_window()

    def add_test_division(self, test_case):
        case = Case(parent=self.scrolled_window, **test_case)
        self.test_container.Add(case.get_division(), 0, wx.EXPAND | wx.ALL, 1)
        self.refresh_scrolled_window()

    def remove_test_division(self, case):
        div = case.get_division()
        self.test_container.Remove(div)

    def refresh_scrolled_window(self):
        self.scrolled_window.SetSizer(self.test_container)
        self.scrolled_sizer.Layout()
