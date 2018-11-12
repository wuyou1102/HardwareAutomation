# -*- encoding:UTF-8 -*-

import Base
import wx
from libs import Utility

import cases


class CaseNameSelection(Base.ListSettingPage):
    def __init__(self, parent):
        Base.ListSettingPage.__init__(self, parent=parent, attr_name="case_name")

    def get_choices(self):
        _type = self._get_value("device_type")
        _class_name = self._get_value("case_class")
        _cls = getattr(cases, _type)
        dir_name = dir(getattr(_cls, _class_name))
        print dir_name
        return Utility.remove_builtins_from_list(dir_name)

    def update(self):
        return False
