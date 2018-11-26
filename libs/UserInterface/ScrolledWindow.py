import wx
from CaseDivision import Case
from libs import Utility
import logging

logger = logging.getLogger(__name__)


class ScrolledWindow(wx.ScrolledWindow):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.VSCROLL):
        wx.ScrolledWindow.__init__(self, parent=parent, id=id, pos=pos, size=size, style=style)
        self._container = wx.BoxSizer(wx.VERTICAL)
        self.scrolled_sizer = parent.scrolled_sizer
        self._test_pool = dict()

    def add_test_division(self, test_case):
        _id = Utility.Random.code(32)
        try:
            case = Case(parent=self, _id=_id, **test_case)
        except Exception, e:
            Utility.Alert.Error(e.message)
            return False
        self._test_pool[_id] = case
        self._add(case.get_division())
        self._refresh()

    def remove_test_division(self, _id):
        if _id in self._test_pool.keys():
            case = self._test_pool.pop(_id)
            self._container.Remove(case.get_division())
            self._refresh()
        else:
            logger.error("Can not find division id:%s" % _id)

    def refresh(self):
        self._refresh()

    def _refresh(self):
        self.SetSizer(self._container, deleteOld=True)
        self.scrolled_sizer.Layout()

    def _add(self, division):
        self._container.Add(division, 0, wx.EXPAND | wx.ALL, 1)
