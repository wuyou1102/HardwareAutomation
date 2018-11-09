# -*- encoding:UTF-8 -*-
from Base import SettingPage


class ShowSummary(SettingPage):
    def __init__(self, parent, test):
        SettingPage.__init__(self, parent=parent)
        self.SetBackgroundColour('blue')
