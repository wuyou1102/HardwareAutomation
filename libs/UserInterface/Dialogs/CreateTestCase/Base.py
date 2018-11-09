# -*- encoding:UTF-8 -*-
from wx.adv import WizardPageSimple


class SettingPage(WizardPageSimple):
    def __init__(self, parent):
        WizardPageSimple.__init__(self, parent)

    def set_value(self):
        raise NotImplementedError
