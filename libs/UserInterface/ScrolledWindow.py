import wx
from CaseDivision import Case


class ScrolledWindow(wx.ScrolledWindow):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.VSCROLL):
        wx.ScrolledWindow.__init__(self, parent=parent, id=id, pos=pos, size=size, style=style)
        self.test_container = parent.test_container
        self.scrolled_sizer = parent.scrolled_sizer

    def add_test_division(self, test_case):
        case = Case(parent=self, **test_case)
        self.test_container.Add(case.get_division(), 0, wx.EXPAND | wx.ALL, 1)
        self.refresh_scrolled_window()

    def remove_test_division(self, division):
        self.test_container.Remove(division)
        self.refresh_scrolled_window()

    def refresh_scrolled_window(self):
        self.SetSizer(self.test_container)
        self.scrolled_sizer.Layout()
